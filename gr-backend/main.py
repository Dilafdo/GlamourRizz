from fastapi import FastAPI, Path
from typing import Optional
from image_generation import generate_image
from prompt import prompt


app = FastAPI()

# @app.get("/generate-image")
# def index():
#     image_path = generate_image("https://glamourizz.s3.eu-north-1.amazonaws.com/trouser/denim-men-llight.webp", prompt = "A girl img wearing a blue dress, CGI, realistic, fhalfull-body, screenshot from party")
#     return {"name": image_path}

# @app.get("/hello")
# def hello():
#     return {"name": "hello world"}

@app.post("/post-prompt")
def post_prompt(data: dict):
    prompt(data["user_id"], data["prompt"], data["gender"], data["image_url"])
    return {"Status": "OK"}

def main():
    images = generate_image("dalle/data/input/sydney.png", prompt = "A girl img wearing a blue dress, CGI, realistic, fhalfull-body, screenshot from party")
    print(images)

if __name__ == "__main__":
    main()
