# civitai-generation

Python library for working with [Civitai](https://civitai.com/) - models for Stable Diffusion 

## Installing
```
pip install git+https://github.com/Lorg0n/civitai-generation-lib/
```

## Usage
```python
from civitai import civitai

cookie = "cookie123abcd" # insert your cookie here
api = civitai.Civitai(cookie)

lora = api.getAdditionalResources("femboi")[0]
lora.setStrength(0.7)

resources = [api.getCheckpoints("OrangeMixs")[0], lora]
params = {
        "prompt": "1girl, yellow-blue colors",
        "negativePrompt": "EasyNegative,sketch,duplicate,ugly,huge eyesm, nsfw",
        "cfgScale": 5.5,
        "sampler": "DPM++ 2M Karras",
        "seed": 372223333,
        "steps": 40,
        "clipSkip": 1,
        "quantity": 4,
        "nsfw": False,
        "aspectRatio": "0",
        "baseModel": "SD1"
}
api.createRequestJson(resources, params)
```

## Description
The library helps to utilize the site's built-in image generation feature with a variety of customization options.

## Cookie
Simply copy the data in the red box and paste this string into the `cookie` variable

![img.png](assets/img.png)