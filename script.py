import bpy
import time
import json

# /Applications/Blender.app/Contents/Resources/3.6/python/bin/python3.10 -m pip install scikit-learn tqdm
from sklearn.model_selection import ParameterGrid
from tqdm import tqdm


C = bpy.context
S = C.scene

outfileName = 'results.txt'
cyclesPrefs = C.preferences.addons['cycles'].preferences

computeDeviceTypes = [
	'METAL',
	'OPTIX',
	'CUDA',
	# 'OPENCL', # was removed
	# 'HIP',
	# 'ONEAPI',
	'NONE',
]


def initMetadataBurning():
	S.render.use_stamp_camera = False
	S.render.use_stamp_date = False
	S.render.use_stamp_filename = False
	S.render.use_stamp_frame = False
	S.render.use_stamp_frame_range = False
	S.render.use_stamp_hostname = False
	S.render.use_stamp_lens = False
	S.render.use_stamp_marker = False
	S.render.use_stamp_memory = False
	S.render.use_stamp_scene = False
	S.render.use_stamp_sequencer_strip = False
	S.render.use_stamp_time = False

	S.render.use_stamp_render_time = True
	S.render.use_stamp_note = True

	S.render.use_stamp = True
	S.render.stamp_font_size = 18


def render(params):
	devType = params['devType']
	cyclesPrefs.compute_device_type = devType
	S.render.stamp_note_text = json.dumps(params, indent=4)
	S.cycles.feature_set = params['featureSet']
	S.cycles.tile_size = params['tileSize']
	S.cycles.shading_system = params['useOSL']

	if devType == 'NONE':
		S.cycles.device = 'CPU'
	else:
		S.cycles.device = 'GPU'

	cyclesPrefs.get_devices()
	# use all devices (gpu and cpu)
	for dev in cyclesPrefs.devices:
		dev['use'] = True
		# print(f"- {dev['name']}")

	startTime = time.time()
	bpy.ops.render.render(use_viewport=True)
	duration = time.time() - startTime
	return duration


def main(f):
	# initMetadataBurning()
	S.render.engine = 'CYCLES'
	S.cycles.use_denoising = False
	S.cycles.use_auto_tile = True
	S.render.use_persistent_data = False

	devTypesSupported = []
	for devType in computeDeviceTypes:
		try:
			cyclesPrefs.compute_device_type = devType
			devTypesSupported.append(devType)
		except TypeError:
			msg = f'{devType} not supported'
			print(msg)
			f.write(f'{msg}\n')

	paramGrid = ParameterGrid([
		{
			'devType': [devType],
			'featureSet': [
				'SUPPORTED',
				'EXPERIMENTAL'
			],
			'tileSize': [
				64,
				128,
				256,
				512,
				1024,
				2048,
				4096
			],
			# OSL only works with CPU and OPTIX
			# although this might change in the future: https://devtalk.blender.org/t/osl-on-gpu/25751
			'useOSL': [True, False] if devType in ['NONE', 'OPTIX'] else [False],
			# NOTE: not sure what effect enabling OSL has when OSL isn't actually used
		}
		for devType in devTypesSupported
	])

	results = []
	for params in tqdm(paramGrid):
		duration = render(params)
		results.append({ **params, 'renderTime': duration })

	print()
	print('###############################')
	print('results:')
	for params in sorted(results, key=lambda x: x['renderTime']):
		duration = params['renderTime']
		del params['renderTime']
		print(f'{duration:.3f}s _ {params}')
		f.write(f'{duration:.3f}s _ {json.dumps(params)}\n')


with open(outfileName, 'w') as f:
	main(f)
