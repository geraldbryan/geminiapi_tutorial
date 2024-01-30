import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

st.title("Welcome to Gemini Chatbot")
st.info("You can see the full source code of this app in this [Github Repositories](https://github.com/geraldbryan/geminiapi_tutorial)", icon="‼️")

# Process and store Query and Response
def llm_function(query):
    # Get Google API Key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Call the Gemini-Pro model
    model = genai.GenerativeModel(model_name = "gemini-pro")
    
    chat = model.start_chat(history=[])
    
    response = chat.send_message(query)

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": response.text
        }
    )

# Initialise session state variables
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

query = st.chat_input("Ask me Anything! 🤖")

if query:
    llm_function(query)

    for message in st.session_state['messages']:
        role = message["role"]
        content = message["content"]
        with st.chat_message(role):
            st.markdown(content)

