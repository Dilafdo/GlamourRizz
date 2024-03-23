import replicate
import os
import cv2
import urllib.request
api = replicate.Client(api_token="r8_B5jSXTTvAatVV49eFMWSV8SZ24thq460VQckx")

def generate_image(image_link, prompt):
    # Load image
    # Download image
    urllib.request.urlretrieve(image_link, "image.jpg")
    image_path = "image.jpg"
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Generate image
    resize1 = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
    PREPRCOESSED_IMAGE_PATH = "dalle/data/out/temp.png"
    cv2.imwrite(PREPRCOESSED_IMAGE_PATH, resize1)
    gray = open(PREPRCOESSED_IMAGE_PATH, "rb")
    output = api.run(
        "tencentarc/photomaker-style:467d062309da518648ba89d226490e02b8ed09b5abc15026e54e31c5a8cd0769",
        input={
            "prompt": prompt + "CGI, realistic, half-body",
            "num_steps": 25,
            "style_name": "Photographic (Default)",
            "input_image": gray,
            "num_outputs": 2,
            "guidance_scale": 3,
            "negative_prompt": "nsfw, worst quality, greyscale, bad anatomy, bad hands, error, text",
            "style_strength_ratio": 20
        }
    )

    return output