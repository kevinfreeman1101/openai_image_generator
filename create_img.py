# create_image.py

import os
import openai
import inquirer

questions = [
    inquirer.List('size',
                  message="What size image would you like to generate?",
                  choices=['256x256', '512x512', '1024x1024'],
                  ),
]
answers = inquirer.prompt(questions)
size=''
if answers['size'] == '256x256':
    size='256x256'
elif answers['size'] == '512x512':
    size='512x512'
elif answers['size'] == '1024x1024':
    size='1024x1024'
else:
    print("error: no answer matched")

PROMPT = input("Enter an image description \n")
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size=size,
)

print(response["data"][0]["url"])
