import google.generativeai as genai
from dotenv import load_dotenv
import os
import PIL.Image

load_dotenv()

# Get Google API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Picture
img = PIL.Image.open('llm/geminipro_api/asset/images.jpeg')

# Call the model
model = genai.GenerativeModel('gemini-pro-vision')

# Add a prompt from and the image
response = model.generate_content(
    [
        "Write a short, engaging blog post based on this picture. It should popularize the places in the photo and make it engaging.", 
        img
    ], 
    stream=True
)
response.resolve()

print(response.text)