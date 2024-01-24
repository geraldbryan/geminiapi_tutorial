import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Get Google API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Call the Gemini-Pro model
model = genai.GenerativeModel(model_name = "gemini-pro")

# Ask a prompt
prompt_parts = [
    "Create a 4 lines poem about AI",
]

response = model.generate_content(prompt_parts)

print(response.text)