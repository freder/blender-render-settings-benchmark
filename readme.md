determine which settings result in the fastest render time

## requirements
- imagemagick


```shell
blender -b /path/to/file.blend \
	-y -noaudio \
	-P ./benchmark.py \
		| ag --invert-match '^Fra:'
# will write results to ./results.txt
```


## Example output

### Apple M2

```
OPTIX not supported
CUDA not supported
0.620s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.623s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.657s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.720s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
0.720s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.723s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.723s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.727s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.727s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.730s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.733s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.733s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.733s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.743s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.770s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.787s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": true, "useTiling": true}
0.800s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.800s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": false}
0.803s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": true}
0.803s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": true}
0.803s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": true, "useTiling": true}
0.807s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": true, "useTiling": true}
0.813s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.817s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": true, "useTiling": true}
0.820s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": false}
0.823s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
0.827s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
0.903s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": true, "useTiling": true}
0.903s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": true, "useTiling": true}
0.943s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
0.947s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
0.957s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
1.030s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": true, "useTiling": true}
1.037s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
1.037s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": true, "useTiling": true}
1.083s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
1.300s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
1.307s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
1.397s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": true, "useTiling": true}
1.400s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": true, "useTiling": true}
1.467s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
1.477s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
1.580s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": true, "useTiling": true}
1.610s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": true, "useTiling": true}
1.703s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
1.793s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
2.270s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
2.353s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
```

### NVIDIA Geforce RTX 2070

```
METAL not supported
0.390s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.417s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.420s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.423s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": true, "useTiling": true}
0.433s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.433s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": true, "useTiling": true}
0.437s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": true}
0.437s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.437s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": false}
0.437s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": false}
0.440s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.440s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.447s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.447s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.460s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": true}
0.460s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
0.460s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.460s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.463s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.467s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": true, "useTiling": true}
0.467s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": true, "useTiling": true}
0.467s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
0.467s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
0.470s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
0.473s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": true, "useTiling": true}
0.487s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": true, "useTiling": true}
0.493s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
0.520s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
0.527s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
0.560s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
0.797s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
0.803s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": true, "useTiling": true}
0.820s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": true, "useTiling": true}
0.823s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
0.840s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
0.863s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
1.207s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": true, "useTiling": true}
1.210s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
1.210s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
1.210s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
1.213s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": true, "useTiling": true}
1.213s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
1.217s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": true, "useTiling": true}
1.217s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
1.217s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": true}
1.217s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
1.217s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": false}
1.223s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": true}
1.223s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
1.223s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": true, "useTiling": true}
1.223s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": false}
1.250s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
1.293s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
1.297s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
1.300s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": true, "useTiling": true}
1.307s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": true, "useTiling": true}
1.313s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
1.333s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": true, "useTiling": true}
1.337s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": true, "useTiling": true}
1.340s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
1.340s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
1.343s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
1.350s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": true, "useTiling": true}
1.350s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
1.410s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
1.410s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": true, "useTiling": true}
1.413s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
1.417s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": true, "useTiling": true}
1.467s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": true, "useTiling": true}
1.520s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
1.530s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
1.550s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
1.923s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
1.943s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": true, "useTiling": true}
1.943s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": true, "useTiling": true}
2.000s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
2.053s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": true, "useTiling": true}
2.070s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": true, "useTiling": true}
2.083s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
2.107s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
```