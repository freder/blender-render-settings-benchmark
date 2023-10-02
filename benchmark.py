import json
import subprocess
import pathlib
import os.path

import bpy

# /Applications/Blender.app/Contents/Resources/3.6/python/bin/python3.10 -m pip install scikit-learn tqdm
from sklearn.model_selection import ParameterGrid
from tqdm import tqdm


scriptDir = pathlib.Path(__file__).parent.resolve()
renderFileName = 'blender-render-settings-benchmark.png'
renderFilePath = os.path.join(scriptDir, renderFileName)
resultsfilePath = os.path.join(scriptDir, 'results.txt')
rounds = 3

computeDeviceTypes = [
	'METAL',
	'OPTIX',
	'CUDA',
	# 'OPENCL', # was removed
	# 'HIP',
	# 'ONEAPI',
	# 'NONE', # ignore CPU
]
devicesToUse = ['all', 'gpu-only']
tileSizes = [
	64,
	128,
	256,
	512,
	1024,
	2048,
	4096
]
featureSets = [
	'SUPPORTED',
	'EXPERIMENTAL'
]


def getUseOslOptions(devType):
	# OSL only works with CPU and OPTIX
	# although this might change in the future: https://devtalk.blender.org/t/osl-on-gpu/25751
	# NOTE: not sure what effect enabling OSL has when OSL isn't actually used
	return [True, False] if devType in ['NONE', 'OPTIX'] else [False]


def initMetadataBurning():
	C = bpy.context
	S = C.scene

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
	C = bpy.context
	S = C.scene
	cyclesPrefs = C.preferences.addons['cycles'].preferences

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

	# NOTE: blender offers no way to get the render time with python
	# however, we can read it from the render image file metadata, using imagemagick
	command = f'identify -verbose \'{renderFilePath}\''
	output = subprocess.check_output(command, shell=True, text=True)

	for line in output.splitlines():
		if 'render_time' in line:
			timecode = line.split('render_time: ')[1]
			duration = timecodeToSeconds(timecode)

	return (duration, enabledDevices)


def main(f):
	C = bpy.context
	S = C.scene
	cyclesPrefs = C.preferences.addons['cycles'].preferences

	initMetadataBurning()

	S.render.engine = 'CYCLES'
	S.cycles.use_denoising = False
	S.render.use_compositing = False
	S.render.use_sequencer = False

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
		configs.append({
			'devType': [devType],
			'devicesToUse': devicesToUse,
			'featureSet': featureSets,
			'useTiling': [True],
			'tileSize': tileSizes,
			# 'useOSL': getUseOslOptions(devType),
		})

		# tiling disabled
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
		for _ in range(rounds):
			dur, enabledDevices = render(params)
			s += dur
		# average over multiple rounds
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


# # make sure file has been loaded
# def load_handler(*args):
# 	print('here')
with open(resultsfilePath, 'w') as f:
	main(f)

# bpy.app.handlers.load_post.append(load_handler)
