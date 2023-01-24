# create_image.py
import os
import openai

PROMPT = input("Enter an image description \n")
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="512x512",
)

print(response["data"][0]["url"])

