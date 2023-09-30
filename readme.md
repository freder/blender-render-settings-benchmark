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

2.886s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 2048, 'useOSL': True}
3.007s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 2048, 'useOSL': True}
3.348s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 2048, 'useOSL': False}
3.361s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 4096, 'useOSL': False}
3.363s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 1024, 'useOSL': False}
3.464s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 512, 'useOSL': False}
3.581s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 4096, 'useOSL': True}
3.655s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 1024, 'useOSL': True}
3.688s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 512, 'useOSL': True}
3.714s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 512, 'useOSL': True}
4.100s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 1024, 'useOSL': False}
4.173s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 1024, 'useOSL': True}
4.237s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 512, 'useOSL': False}
5.217s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 4096, 'useOSL': True}
5.440s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 2048, 'useOSL': False}
5.781s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 4096, 'useOSL': False}
6.851s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 256, 'useOSL': False}
6.888s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 256, 'useOSL': True}
6.909s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 256, 'useOSL': True}
6.931s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 256, 'useOSL': False}
8.188s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 128, 'useOSL': True}
8.390s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 128, 'useOSL': False}
8.393s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 128, 'useOSL': True}
8.613s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 128, 'useOSL': False}
11.618s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 64, 'useOSL': False}
11.806s _ {'devType': 'METAL', 'featureSet': 'SUPPORTED', 'tileSize': 64, 'useOSL': True}
12.257s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 64, 'useOSL': False}
12.829s _ {'devType': 'METAL', 'featureSet': 'EXPERIMENTAL', 'tileSize': 64, 'useOSL': True}
```

### nvidia geforce rtx 2070

```
METAL not supported

1.331s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 2048, 'useOSL': true}
1.360s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 4096, 'useOSL': true}
1.404s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 2048, 'useOSL': true}
1.420s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 4096, 'useOSL': true}
1.443s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 2048, 'useOSL': false}
1.445s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 4096, 'useOSL': false}
1.507s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 4096, 'useOSL': false}
1.547s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 4096, 'useOSL': true}
1.574s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 2048, 'useOSL': false}
1.665s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 2048, 'useOSL': false}
1.671s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 4096, 'useOSL': false}
1.673s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 4096, 'useOSL': false}
1.686s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 2048, 'useOSL': false}
1.697s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 2048, 'useOSL': true}
1.719s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 1024, 'useOSL': false}
1.801s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 2048, 'useOSL': true}
1.805s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 1024, 'useOSL': true}
1.818s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 1024, 'useOSL': true}
1.837s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 4096, 'useOSL': true}
1.838s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 1024, 'useOSL': true}
1.841s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 1024, 'useOSL': true}
1.852s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 1024, 'useOSL': false}
1.912s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 1024, 'useOSL': false}
1.947s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 1024, 'useOSL': false}
1.972s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 512, 'useOSL': false}
1.972s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 512, 'useOSL': false}
2.008s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 512, 'useOSL': true}
2.024s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 512, 'useOSL': true}
2.089s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 512, 'useOSL': true}
2.089s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 512, 'useOSL': true}
2.090s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 512, 'useOSL': false}
2.187s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 512, 'useOSL': false}
2.286s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 256, 'useOSL': true}
2.310s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 256, 'useOSL': true}
2.485s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 256, 'useOSL': false}
2.512s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 256, 'useOSL': false}
2.788s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 128, 'useOSL': true}
2.791s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 256, 'useOSL': true}
2.814s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 256, 'useOSL': false}
2.815s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 256, 'useOSL': true}
2.850s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 128, 'useOSL': true}
2.891s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 256, 'useOSL': false}
3.042s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 128, 'useOSL': false}
3.099s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 128, 'useOSL': true}
3.146s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 128, 'useOSL': false}
3.184s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 128, 'useOSL': false}
3.217s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 128, 'useOSL': false}
3.242s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 128, 'useOSL': true}
3.538s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 64, 'useOSL': true}
3.659s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 64, 'useOSL': false}
3.688s _ {'devType': 'CUDA', 'featureSet': 'SUPPORTED', 'tileSize': 64, 'useOSL': false}
3.736s _ {'devType': 'CUDA', 'featureSet': 'EXPERIMENTAL', 'tileSize': 64, 'useOSL': true}
3.988s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 64, 'useOSL': true}
4.053s _ {'devType': 'OPTIX', 'featureSet': 'EXPERIMENTAL', 'tileSize': 64, 'useOSL': false}
4.099s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 64, 'useOSL': true}
4.212s _ {'devType': 'OPTIX', 'featureSet': 'SUPPORTED', 'tileSize': 64, 'useOSL': false}
```