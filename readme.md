Script to determine which settings result in the fastest render time (for a given .blend file)


## Requirements
- python packages (installed for Blender's python):
	- tqdm
	- scikit-learn
- imagemagick


## Configure
Edit [settings.py](./settings.py) to your liking.

- Device type: `CUDA` / `OPTIX` / `METAL`
- Devices to use: `all` / `gpu-only`
- Feature set: `EXPERIMENTAL` / `SUPPORTED`
- Tiling: `on` / `off`
- Tile size: `64` / `128` / `256` / `512` / `1024` / `2048` / `4096` (only used if tiling is enabled)
- Rounds: `3` (number of runs to take the average render time of)


## Run
```shell
# add more args as needed: https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html
time \
	blender --factory-startup -noaudio -y \
		-b /path/to/file.blend \
		--scene 'Scene' \
		-P ./benchmark.py \
	| ag --invert-match '^Fra:'
# will write results to ./results.txt
```


## Example output

### Apple M2

```
OPTIX not supported
CUDA not supported
0.310s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.317s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 2048, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.317s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 4096, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.317s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.317s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": false, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.323s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.327s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.327s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": false, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.437s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.440s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 512, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.580s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.583s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 256, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
0.743s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.750s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 2048, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.760s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 512, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.780s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.810s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 4096, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.830s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": false, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.833s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": false, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.840s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.840s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.863s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
0.940s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 256, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
1.040s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
1.053s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 128, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
1.053s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
1.480s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 64, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
1.487s _ {"devType": "METAL", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useTiling": true, "enabledDevices": {"Apple M2 Pro": false, "Apple M2 Pro (GPU - 16 cores)": true}}
1.660s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 128, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
1.830s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
2.323s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 64, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
2.337s _ {"devType": "METAL", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useTiling": true, "enabledDevices": {"Apple M2 Pro": true, "Apple M2 Pro (GPU - 16 cores)": true}}
```

### NVIDIA Geforce RTX 2070

```
METAL not supported
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.160s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.280s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.283s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.303s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.317s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.430s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.430s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.433s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.437s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.440s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.447s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.453s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.453s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.457s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.470s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.473s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.497s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 4096, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.500s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.503s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 1024, "useTiling": false, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.507s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.510s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 2048, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.523s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.527s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.533s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.550s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.550s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.550s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
0.563s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.563s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.783s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.807s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.817s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
0.830s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 256, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.133s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.133s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.167s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.167s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.170s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.177s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.183s _ {"devType": "CUDA", "devicesToUse": "gpu-only", "featureSet": "SUPPORTED", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.210s _ {"devType": "OPTIX", "devicesToUse": "gpu-only", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": false}}
1.313s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.333s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.347s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.347s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.493s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.533s _ {"devType": "OPTIX", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.547s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "SUPPORTED", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
1.550s _ {"devType": "CUDA", "devicesToUse": "all", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useTiling": true, "enabledDevices": {"NVIDIA GeForce RTX 2070": true, "AMD Ryzen 5 2600 Six-Core Processor": true}}
```