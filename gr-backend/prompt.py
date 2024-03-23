from openapi import generate_ids
from image_generation import generate_image
import json
import os
def call_prompt(user_id, prompt, gender, image_url):
    with open("bottom.json", "r") as file:
        bottom_data = json.load(file)

    with open("top.json", "r") as file:
        top_data = json.load(file)

    with open("jewellery.json", "r") as file:
        jewellery_data = json.load(file)

    with open("output.json", "r") as file:
        output_data = json.load(file)

    data_obj = {
        "bottom": bottom_data,
        "top": top_data,
        "jewellery": jewellery_data
    }

    # Find the matching ids
    result = generate_ids(data_obj, prompt, gender)
    print("======================== ", result["status"])
    while result["status"] == "FAIL":
        result = generate_ids(data_obj, prompt, gender)
        print("======================== ", result["status"])
    # print(user_id)
    # print(result)
    filename = image_url.split("/")[-1]

    # Remove the file extension
    name = os.path.splitext(filename)[0]

    prompt_str = f"This is {name}. {result['new_prompt']}"
    print(prompt_str)
    image_path = generate_image(image_url, prompt_str)

    # Create JSON object
    json_object = {
        "id": user_id,
        "image_url_1": image_path[0],
        "image_url_2": image_path[1]
    }

    print("JSON Object: ", json_object)

    output_data.append(json_object)
    with open("output.json", "w") as file:
        json.dump(output_data, file, indent=4)

    # return {"name": image_path}

    # return result

