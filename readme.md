determine which settings result in the fastest render time

```shell
blender -b -y -noaudio \
	-P ./script.py \
	/path/to/file.blend \
		| ag --invert-match '^Fra:'
```


## example output

### apple M2

```
OPTIX not supported
CUDA not supported
3.749s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
3.822s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
3.958s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
3.974s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
4.349s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
4.554s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
4.588s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
4.715s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
4.811s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
5.444s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
5.446s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
5.456s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
5.458s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
5.477s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
5.495s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
5.569s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
5.573s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
5.593s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
5.653s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
5.742s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
5.770s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
5.903s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
6.059s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": true, "useTiling": true}
6.071s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": true, "useTiling": true}
6.077s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": false}
6.084s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": true, "useTiling": true}
6.109s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": true, "useTiling": true}
6.124s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": true, "useTiling": true}
6.151s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": true, "useTiling": true}
6.181s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": true}
6.253s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": true}
6.324s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": false}
6.396s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
6.419s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": true, "useTiling": true}
6.423s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
6.517s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": true, "useTiling": true}
6.693s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
7.252s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
7.253s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": true, "useTiling": true}
7.314s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": true, "useTiling": true}
7.417s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
7.448s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
8.284s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
8.478s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": true, "useTiling": true}
8.496s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
8.508s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": true, "useTiling": true}
12.051s _ {"devType": "METAL", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
12.342s _ {"devType": "METAL", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
```

### nvidia geforce rtx 2070

```
METAL not supported
1.365s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
1.409s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
1.419s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
1.460s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
1.487s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": true, "useTiling": true}
1.503s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": true, "useTiling": true}
1.511s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
1.546s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
1.572s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": true, "useTiling": true}
1.573s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
1.585s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": true, "useTiling": true}
1.594s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
1.601s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
1.619s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
1.645s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
1.667s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
1.671s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": false}
1.736s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": false}
1.798s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
1.809s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": true}
1.909s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
1.999s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
2.002s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
2.038s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
2.046s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": true, "useTiling": true}
2.052s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
2.083s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": true, "useTiling": true}
2.089s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
2.132s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
2.184s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": true}
2.307s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
2.338s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
2.628s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": true, "useTiling": true}
2.674s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": true, "useTiling": true}
2.767s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
2.781s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
2.909s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
2.920s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
3.099s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": true, "useTiling": true}
3.165s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
3.188s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": true, "useTiling": true}
3.193s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
3.689s _ {"devType": "CUDA", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
3.701s _ {"devType": "CUDA", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
4.115s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": true, "useTiling": true}
4.164s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
4.200s _ {"devType": "OPTIX", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
4.224s _ {"devType": "OPTIX", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": true, "useTiling": true}
9.113s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": true, "useTiling": true}
9.125s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": true, "useTiling": true}
9.128s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 512, "useOSL": false, "useTiling": true}
9.137s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 512, "useOSL": false, "useTiling": true}
9.335s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": true, "useTiling": true}
9.348s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 256, "useOSL": false, "useTiling": true}
9.369s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": true, "useTiling": true}
9.369s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 256, "useOSL": false, "useTiling": true}
9.396s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": false}
9.408s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": false}
9.423s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": false, "useTiling": true}
9.423s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": true, "useTiling": true}
9.436s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": false}
9.438s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": false, "useTiling": true}
9.439s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": false}
9.444s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": true, "useTiling": true}
9.447s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 4096, "useOSL": true, "useTiling": true}
9.449s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 2048, "useOSL": true, "useTiling": true}
9.454s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 4096, "useOSL": false, "useTiling": true}
9.466s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 2048, "useOSL": false, "useTiling": true}
9.575s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": false, "useTiling": true}
9.580s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": false, "useTiling": true}
9.588s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 1024, "useOSL": true, "useTiling": true}
9.592s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 1024, "useOSL": true, "useTiling": true}
10.026s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": true, "useTiling": true}
10.031s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 128, "useOSL": false, "useTiling": true}
10.034s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": true, "useTiling": true}
10.082s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 128, "useOSL": false, "useTiling": true}
11.314s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": false, "useTiling": true}
11.314s _ {"devType": "NONE", "featureSet": "EXPERIMENTAL", "tileSize": 64, "useOSL": true, "useTiling": true}
11.315s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": false, "useTiling": true}
11.327s _ {"devType": "NONE", "featureSet": "SUPPORTED", "tileSize": 64, "useOSL": true, "useTiling": true}
```