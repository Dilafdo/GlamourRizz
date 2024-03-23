from openapi import generate_ids
from image_generation import generate_image
import json
def prompt(user_id, prompt, gender):
    with open("bottom.json", "r") as file:
        bottom_data = json.load(file)

    with open("top.json", "r") as file:
        top_data = json.load(file)

    with open("jewellery.json", "r") as file:
        jewellery_data = json.load(file)

    data_obj = {
        "bottom": bottom_data,
        "top": top_data,
        "jewellery": jewellery_data
    }

    # Find the matching ids
    result = generate_ids(data_obj, prompt, gender)
    while result["status"] == "FAIL":
        result = generate_ids(data_obj, prompt, gender)
    # print(user_id)
    # print(result)
    generate_image(image_path, result["new_prompt"])

    return result

