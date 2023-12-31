import sys
import json
import subprocess
import pathlib
import os.path

import bpy

# /Applications/Blender.app/Contents/Resources/3.6/python/bin/python3.10 -m pip install scikit-learn tqdm
from sklearn.model_selection import ParameterGrid
from tqdm import tqdm

scriptDir = str(
	pathlib.Path(__file__).parent.resolve()
)

sys.path.append(scriptDir)
from settings import (
	additionalInit,
	rounds,
	computeDeviceTypes,
	devicesToUse,
	useTiling,
	tileSizes,
	featureSets
)


renderFileName = 'blender-render-settings-benchmark.png'
renderFilePath = os.path.join(scriptDir, renderFileName)
resultsfilePath = os.path.join(scriptDir, 'results.txt')

C = bpy.context
S = C.scene
cyclesPrefs = C.preferences.addons['cycles'].preferences


# def getUseOslOptions(devType):
# 	# OSL only works with CPU and OPTIX
# 	# although this might change in the future: https://devtalk.blender.org/t/osl-on-gpu/25751
# 	# NOTE: not sure what effect enabling OSL has when OSL isn't actually used
# 	return [True, False] if devType in ['NONE', 'OPTIX'] else [False]


def initMetadataBurning():
	S.render.use_stamp_camera = False
	S.render.use_stamp_date = False
	S.render.use_stamp_filename = False
	S.render.use_stamp_frame = False
	S.render.use_stamp_frame_range = False
	S.render.use_stamp_lens = False
	S.render.use_stamp_marker = False
	S.render.use_stamp_memory = False
	S.render.use_stamp_scene = False
	S.render.use_stamp_sequencer_strip = False
	S.render.use_stamp_time = False

	S.render.use_stamp_hostname = True
	S.render.use_stamp_render_time = True
	S.render.use_stamp_note = True

	S.render.use_stamp = True
	S.render.stamp_font_size = 18


def timecodeToSeconds(timecode):
	# timecode is in format mm:ss.ms
	mins, secs = timecode.split(':')
	return int(mins) * 60 + float(secs)


def render(params):
	devType = params['devType']
	cyclesPrefs.compute_device_type = devType
	S.cycles.feature_set = params['featureSet']
	S.cycles.use_auto_tile = params['useTiling']
	S.cycles.tile_size = params['tileSize']
	# S.cycles.shading_system = params['useOSL']

	if devType == 'NONE':
		S.cycles.device = 'CPU'
	else:
		S.cycles.device = 'GPU'

	cyclesPrefs.get_devices()

	cpuDevices = list(map(
		lambda dev: dev.id,
		cyclesPrefs.get_devices_for_type('CPU')
	))
	enabledDevices = {}
	for dev in cyclesPrefs.devices:
		if params['devicesToUse'] == 'all':
			dev['use'] = True
		else:
			# only use gpu
			dev['use'] = dev.id not in cpuDevices
		enabledDevices[dev['name']] = dev['use']

	S.render.stamp_note_text = json.dumps({
		**params,
		'enabledDevices': enabledDevices,
	}, indent=4)

	bpy.ops.render.render(write_still=True)
	duration = -1

	# NOTE: blender offers no way to get the render time with python.
	# however, we can read it from the render image file metadata, using imagemagick
	command = f'identify -verbose \'{renderFilePath}\''
	output = subprocess.check_output(command, shell=True, text=True)

	for line in output.splitlines():
		if 'render_time' in line:
			timecode = line.split('render_time: ')[1]
			duration = timecodeToSeconds(timecode)

	return (duration, enabledDevices)


def main(f):
	initMetadataBurning()
	additionalInit(S)

	S.render.filepath = renderFilePath
	S.render.image_settings.file_format = 'PNG'
	S.render.use_overwrite = True

	devTypesSupported = []
	for devType in computeDeviceTypes:
		try:
			cyclesPrefs.compute_device_type = devType
			devTypesSupported.append(devType)
		except TypeError:
			msg = f'{devType} not supported'
			print(msg)
			f.write(f'{msg}\n')

	configs = []
	for devType in devTypesSupported:
		# tiling enabled
		if True in useTiling:
			configs.append({
				'devType': [devType],
				'devicesToUse': devicesToUse,
				'featureSet': featureSets,
				'useTiling': [True],
				'tileSize': tileSizes,
				# 'useOSL': getUseOslOptions(devType),
			})

		# tiling disabled
		if False in useTiling:
			configs.append({
				'devType': [devType],
				'devicesToUse': devicesToUse,
				'featureSet': featureSets,
				'useTiling': [False],
				'tileSize': [1024], # not used, so whatever
				# 'useOSL': getUseOslOptions(devType),
			})

	paramGrid = ParameterGrid(configs)

	results = []
	for params in tqdm(paramGrid):
		s = 0
		enabledDevices = {}
		# take the average over multiple rounds
		for _ in range(rounds):
			dur, enabledDevices = render(params)
			s += dur
		duration = s / rounds
		results.append({
			**params,
			'renderTime': duration,
			'enabledDevices': enabledDevices,
		})

	print()
	print('###############################')
	print('results:')
	for params in sorted(results, key=lambda p: p['renderTime']):
		duration = params['renderTime']
		del params['renderTime']
		d = f'{duration:.3f}s'
		print(f'{d} _ {params}')
		f.write(f'{d} _ {json.dumps(params)}\n')


with open(resultsfilePath, 'w') as f:
	main(f)
