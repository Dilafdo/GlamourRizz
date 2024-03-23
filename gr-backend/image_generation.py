import replicate
import os
import cv2
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

async def generate_image(image_path):
    # Load image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Generate image
    resize1 = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
    PREPRCOESSED_IMAGE_PATH = "dalle/data/out/temp.png"
    cv2.imwrite(PREPRCOESSED_IMAGE_PATH, resize1)
    gray = open(PREPRCOESSED_IMAGE_PATH, "rb")
    output = api.run(
        "tencentarc/photomaker-style:467d062309da518648ba89d226490e02b8ed09b5abc15026e54e31c5a8cd0769",
        input={
            "prompt": "A girl img wearing a necklace gold with green gems and red dress, CGI, realistic, full-body, busty, screenshot from party",
            "num_steps": 25,
            "style_name": "Photographic (Default)",
            "input_image": gray,
            "num_outputs": 1,
            "guidance_scale": 3,
            "negative_prompt": "nsfw, worst quality, greyscale, bad anatomy, bad hands, error, text",
            "style_strength_ratio": 30
        }
    )
    output[0].download("data/out/output.png")
    return "data/out/output.png"