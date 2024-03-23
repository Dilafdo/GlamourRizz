from openai import OpenAI
import json
client = OpenAI(api_key="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")


def generate_ids(data_obj, user_prompt, gender):
  completion = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
      {"role": "system", "content": "You will be provided with a json style text with different types of fashion clothing types. \\\
                                    the text contains a type of the dress/jewellery and in each type there will be a list of different types of \\\
                                    clothing with an id number and a description of explaining the type in details.\\\
                                    Also you will be provided with a text prompt containing a description from a user. Your task is to \\\
                                    to find matching clothing types mention in the text prompt from the json text object and return the ids of\\\
                                    those that matches and the description and a new prompt that more suitable with all the information of the matches in a json style.\\\
                                    If the prompt does not contain all the information about the top dress, bottom dress and the jewellery, suggest the missing ones. every prompt should include info about top, bottom and jewellery.\\\
                                    Additionally, extract a background information from the new prompt or if there is no background info choose something suitable and inlude it with the new prompt itself.\\\
                                    Always make sure the new prompt is a single sentence and also embed the gender information.\\\
                                    output json string should be this format - '{matching_ids: [], matching_descriptions:[], new_prompt: string}'. Keep the new prompt as a way to use to generate an image out of it"},
      {"role": "user", "content": f"json text: {str(data_obj)}, prompt: {str(user_prompt)}, gender: {str(gender)}"}
    ]
  )
  
  ret_prompt = completion.choices[0].message.content
  print(ret_prompt)

  if ret_prompt:
      json_string = ret_prompt.replace("'", "\"")

      try:
          # Try to load the JSON object
          json_object = json.loads(json_string)

          matching_ids = json_object.get('matching_ids', [])
          new_prompt = "img - " + json_object.get('new_prompt', '')

          print(f'matching ids: {matching_ids}')
          print(f'new prompt: {new_prompt}')

          return {"status": "OK", "new_prompt": new_prompt, "matching_ids": matching_ids}
      except json.JSONDecodeError as e:
          print(f'Error decoding JSON: {e}')
          return {"status": "FAIL"}
  else:
      print('Returned prompt is empty.')
      return {"status": "FAIL"}
  
def chatopenai(previous_prompt, options):

  completion = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
      {"role": "system", "content": "You will be provided with a json style text with different types of fashion clothing types. \\\
                                    the text contains a type of the dress/jewellery and in each type there will be a list of different types of \\\
                                    clothing with an id number and a description of explaining the type in details.\\\
                                    Also you will be provided with a text containing a previous text prompt generated and a new features list. Combine the new feature list to the prompt and replace the new features. Your task is to \\\
                                    to find matching clothing types mention in the text prompt + new features list from the json text object and return the ids of\\\
                                    those that matches and the description and a new prompt that more suitable with all the information of the matches in a json style.\\\
                                    Additionally, extract a background information from the new prompt or if there is no background info choose something suitable and inlude it with the new prompt itself.\\\
                                    Always make sure the new prompt is a single sentence and also embed the gender information.\\\
                                    output json string should be this format - '{matching_ids: [], matching_descriptions:[], new_prompt: string}' . Keep the new prompt as a way to use to generate an image out of it"},
      {"role": "user", "content": f"json text: {str(data_obj)}, previous_prompt: {str(previous_prompt)}, options: {str(options)}"}
    ]
  )
  
  ret_prompt = completion.choices[0].message.content
  print(ret_prompt)

  return 0

data_obj = {
  "top": [{
    "id": "65fed029ee93fb64358fd8fc",
    "description": "frock, short dress, only upto knees, red, for women",
    "img-url": "https://glamourizz.s3.eu-north-1.amazonaws.com/frock/red+short.webp"
  },
  {
    "id": "65fed029ee93fb64358fd8fd",
    "description": "frock, long dress, only upto knees, blue, for women",
    "img-url": "https://glamourizz.s3.eu-north-1.amazonaws.com/frock/blue+long.webp"
  },
  {
    "id": "65fed029ee93fb64358fd8fe",
    "description": "shirt, long sleeve, checks, blue, for men",
    "img-url": "https://glamourizz.s3.eu-north-1.amazonaws.com/shirt/blue+long.webp"
  },
  {
    "id": "65fed029ee93fb64358fd8ff",
    "description": "shirt, short sleeve, vertical lines, red, for men",
    "img-url": "https://glamourizz.s3.eu-north-1.amazonaws.com/shirt/red+short.webp"
  }],
  "bottom": [{
    "id": "65fed03cee93fb64358fd902",
    "description": "trouser, for men, light-blue, denim, 100% cotton, slim fit",
    "img-url": "https://glamourizz.s3.eu-north-1.amazonaws.com/trouser/denim-men-llight.webp"
  },
  {
    "_id": "65fed03cee93fb64358fd903",
    "description": "trouser, for men, black, 100% cotton, regular fit",
    "img-url": "https://glamourizz.s3.eu-north-1.amazonaws.com/trouser/black+trouser.webp"
  }],
  "jewellery": [
    {
      "id": 5,
      "Description": "gold jewellery with diamond stones"
    },
    {
      "id": 6,
      "Description": "gold jewellery with gem stones"
    }
  ],
  
}

prompt = "I want to dress myself with white trouser I like to see myself in a sunny beach area"
gender = "men"
new_obj = generate_ids(data_obj=data_obj, user_prompt=prompt, gender=gender)



old_prompt = new_obj["new_prompt"]

chatopenai(old_prompt, ["red dress", "gold jewellery"])




