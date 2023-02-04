# How to Use this Script (Linux & Mac Users)

1. Use the RealPython instructions [here](https://realpython.com/generate-images-with-dalle-openai-api/#get-your-openai-api-key) to obtain an API key for using Dall-E 2.
2. Append the following to your ~/.bashrc or ~/.bash_profile:

```
## OpenAI API Key
export OPENAI_API_KEY="replace-this-text-with-your-key"
```

3. Source your terminal to load the key into your environment by typing `source ~/.bashrc`

4. Create a python environment using Python 3.7.1 or higher and install the libraries listed in requirements.txt . Need help with Python environments? Check out [this](https://realpython.com/python-virtual-environments-a-primer/) tutorial.
5. With your environment activated, type `pip install -r requirements.txt`
6. With everything installed, execute the included scripts with python. For instance, type `python create_img.py`; choose an image size when prompted; then type the keywords and/or description of the image you would like generated and press return. When the script completes, it will return the url of your image.
7. Want to learn more? Check out the [demo](https://openai.com/dall-e-2/) or read up on the [API 
   docs](https://platform.openai.com/docs/guides/images) on the OpenAI website.
