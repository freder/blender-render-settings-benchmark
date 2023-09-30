import bpy
import time
import json

# /Applications/Blender.app/Contents/Resources/3.6/python/bin/python3.10 -m pip install scikit-learn tqdm
from sklearn.model_selection import ParameterGrid
from tqdm import tqdm


C = bpy.context
S = C.scene
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

devTypesSupported = []
for devType in computeDeviceTypes:
	try:
		cyclesPrefs.compute_device_type = devType
		devTypesSupported.append(devType)
	except TypeError:
		print(f'{devType} not supported')

paramGrid = ParameterGrid([
	{
		'devType': devTypesSupported,
		'featureSet': [
			'SUPPORTED',
			'EXPERIMENTAL'
		],
		'tileSize': [
			# 32,
			64,
			128,
			256,
			512,
			1024,
			2048,
			4096
		],
		# 'persistentData': [True, False],
		'useOSL': [
			True,
			False
		],
	}
])


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


# initMetadataBurning()
S.render.engine = 'CYCLES'
S.cycles.use_denoising = False
S.cycles.use_auto_tile = True
S.render.use_persistent_data = False

results = []
for params in tqdm(paramGrid):
	duration = render(params)
	results.append({
		**params,
		'renderTime': duration
	})

print()
print('###############################')
print('results:')

for params in sorted(results, key=lambda x: x['renderTime']):
	duration = params['renderTime']
	del params['renderTime']
	print(f"{duration:.3f}s _ {params}")
