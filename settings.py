rounds = 3

computeDeviceTypes = [
	# 'NONE', # CPU
	'METAL',
	'OPTIX',
	'CUDA',
	# 'HIP',
	# 'ONEAPI',
	# 'OPENCL', # was removed from blender at some point
]

devicesToUse = [
	'all',
	'gpu-only'
]

useTiling = [
	True,
	False
]

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


def additionalInit(scene):
	scene.render.engine = 'CYCLES'
	scene.render.resolution_percentage = 100
	# none of the extra stuff:
	scene.cycles.use_denoising = False
	scene.render.use_compositing = False
	scene.render.use_sequencer = False
