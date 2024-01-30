import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Get Google API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Call the Gemini-Pro model
chat_model = genai.GenerativeModel(model_name = "gemini-pro")

chat = chat_model.start_chat(history=[])

response = chat.send_message("Give me the best place in Indonesia to be visited in 2024")
print(response.text)

response_1 = chat.send_message("From that place give me a 5 point why I should visit that place")
print(response_1.text)

response_2 = chat.send_message("From that same place give me a 5 point why I should never visit that place")
print(response_2.text)

print(chat.history)