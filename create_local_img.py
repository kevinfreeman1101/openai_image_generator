# create_image.py

import os
import openai
import inquirer
import json
from pathlib import Path

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
