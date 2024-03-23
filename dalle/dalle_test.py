import openai
import os
import cv2
import urllib.request

# OpenAI.api_key = os.getenv('OPENAI_API_KEY')
# openai.api_key = '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'
openai.api_key = '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'

# completion = openai.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

PREPRCOESSED_IMAGE_PATH = "data/out/gray.png"

# print(completion.choices[0].message)
image = cv2.imread("data/input/sydney.png", cv2.IMREAD_COLOR)
# rgba = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
# Convert the image to black and white
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# Save the black and white image
cv2.imwrite(PREPRCOESSED_IMAGE_PATH, gray)


response = openai.images.edit(
  model="dall-e-2",
  image=open(PREPRCOESSED_IMAGE_PATH, "rb"),
#   mask=open("mask.png", "rb"),
  prompt="Red dress girl with a white hat in a field of flowers.",
  n=1,
#   style='natural',
#   quality="standard",
  size="256x256"
)
image_url = response.data[0].url
print(image_url)
# # Download the image using the image_url
image_path = "data/out/image.jpg"  # Provide the desired path to save the image
urllib.request.urlretrieve(image_url, image_path)

# # Read and display the image using OpenCV
image = cv2.imread(image_path)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()