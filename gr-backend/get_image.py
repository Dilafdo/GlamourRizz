import json

def get_image_from_userId(user_id):
    with open("output.json", "r") as file:
        output_data = json.load(file)

    image_url = find_image_url_by_id(output_data, user_id)
    if image_url is None:
        return {"status": "FAIL"}
    else:
        return {"status": "OK", "image_url": image_url}


def find_image_url_by_id(data, target_id):
    lst = []
    for item in data:
        if item['id'] == target_id:
            lst.append(item['image_url_1'])
            lst.append(item['image_url_2'])
            return lst
    return None


