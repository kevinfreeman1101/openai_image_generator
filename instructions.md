# How to Use this Script (Linux & Mac Users)

1. Use the RealPython instructions [here](https://realpython.com/generate-images-with-dalle-openai-api/#get-your-openai-api-key) to obtain an API key for using Dall-E 2.
2. Append the following to your ~/.bashrc file:

```
## OpenAI API Key
export OPENAI_API_KEY="replace-this-text-with-your-key"
```

3. Source your terminal to load the key into your environment by typing `source ~/.bashrc`

4. Create a python environment using Python 3.7.1 or higher and install the libraries listed in requirements.txt . Need help with Python environments? Check out [this](https://realpython.com/python-virtual-environments-a-primer/) tutorial.
5. With your environment activated, type `pip install -r requirements.txt`
6. With everything installed, execute the included scripts with python. For instance, to generate a 1024x1024 image, type `python create_1024_img.py`; when prompted for text, type the keywords and/or description of the image you would like generated and press return. When the script completes, it will return the url of your image.