from fastapi import FastAPI, Path
from typing import Optional
from image_generation import generate_image


app = FastAPI()

@app.get("/generate-image")
def index():
    image_path = generate_image("dalle/data/input/sydney.png", prompt = "A girl img wearing a blue dress, CGI, realistic, fhalfull-body, screenshot from party")
    return {"name": image_path}

@app.post("post-prompt")
def post_prompt(user_id: int, prompt: str, gendre: str):
    return {"success": "Ok"}

def main():
    images = generate_image("dalle/data/input/sydney.png", prompt = "A girl img wearing a blue dress, CGI, realistic, fhalfull-body, screenshot from party")
    print(images)

if __name__ == "__main__":
    main()
