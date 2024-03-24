from fastapi import FastAPI, Path
from image_generation import generate_image
import uvicorn

from prompt import call_prompt
from get_image import get_image_from_userId

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello():
    return {"name": "hello world"}

@app.post("/post-prompt")
def post_prompt(data: dict):
    # loop = asyncio.get_event_loop()
    call_prompt(data["user_id"], data["prompt"], data["gender"], data["image_url"])
    return {"status": "OK"}

@app.get("/get-url/{user_id}")
def get_url(user_id: int = Path(..., title="The ID of the user")):
    return get_image_from_userId(user_id)

def main():
    images = generate_image("dalle/data/input/sydney.png", prompt = "A girl img wearing a blue dress, CGI, realistic, fhalfull-body, screenshot from party")
    print(images)

# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
 uvicorn.run("main:app", host="0.0.0.0", port=8000)