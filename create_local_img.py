# create_image.py

import os
import openai
import inquirer
from pathlib import Path
import json
from base64 import b64decode


data_dir = Path.cwd() / "openai_responses"
data_dir.mkdir(exist_ok=True)

questions = [
    inquirer.List('size',
                  message="What size image would you like to generate?",
                  choices=['256x256', '512x512', '1024x1024'],
                  ),
    inquirer.List('count',
                  message="How many images would you like to generate?",
                  choices=['1', '2', '3', '4', '5', '6', '7', '8',
                           '9,', '10'],
                  ),
]
answers = inquirer.prompt(questions)
size = answers['size']
count = int(answers['count'])

PROMPT = input("Enter an image description \n")
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
    prompt=PROMPT,
    n=count,
    size=size,
    response_format="b64_json",
)

# Write data to JSON file
file_name = data_dir / f"{PROMPT[:15]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)

# Convert JSON file to img; save in images directory
json_file = Path(file_name)
image_dir = Path.cwd() / "openai_responses" / "images" / json_file.stem
image_dir.mkdir(parents=True, exist_ok=True)

with open(json_file, mode="r", encoding="utf-8") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = image_dir / f"{json_file.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)
