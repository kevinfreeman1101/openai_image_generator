# How to Use this Script (Linux & Mac Users)
Many thanks to Martin Breuss for composing the excellent [RealPython](https://realpython.com/generate-images-with-dalle-openai-api/) 
article that served as the basis for this repo. Check out [his 
website](https://www.martinbreuss.com/) if you're looking for a 
seriously talented Python developer.

## Instructions

1. Use the RealPython instructions [here](https://realpython.com/generate-images-with-dalle-openai-api/#get-your-openai-api-key) to obtain an API key for using Dall-E 2.
2. Append the following to your ~/.bashrc or ~/.bash_profile:

```
## OpenAI API Key
export OPENAI_API_KEY="replace-this-text-with-your-key"
```

3. Source your terminal to load the key into your environment by typing `source ~/.bashrc` or `source ~/.bash_profile`, depending on which file your system uses.

4. Create a python environment using Python 3.9 and install the libraries listed in requirements.txt . Need help with Python environments? Check out [this](https://realpython.com/python-virtual-environments-a-primer/) tutorial.
5. With your environment activated, type `pip install openai`
6. After install of openai completes, type `pip install -r requirements.txt`
7. With everything installed, execute the included scripts with python. For instance, type `python create_local_img.py`; choose an image size when prompted; then type the keywords and/or description of the image you would like generated and press return. When the script completes, it will save the response as a JSON b64 file, then generate PNG images and save them in an `images` directory.
8. Alternative to step 7: type `python create_imgurl.py` to generate image urls that you can view in a browser.
9. Want to learn more? Check out the [demo](https://openai.com/dall-e-2/) or read the [API 
   docs](https://platform.openai.com/docs/guides/images) on the OpenAI website.
