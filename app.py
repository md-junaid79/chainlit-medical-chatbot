# app.py
import chainlit as cl
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    raise Exception("Gemini API key not found. Please set GOOGLE_API_KEY in your .env file.")

# Configure Gemini API with your key
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-2.0-flash")
# Optionally, start a chat session if your usage requires maintaining conversation history
chat = model.start_chat(history=[])


async def main(message: cl.Message):
    # Build a prompt that instructs the model to act as a helpful medical assistant
    prompt = (
        "your name is CyberHeal and you are a helpful medical assistant."
        "Provide concise and accurate medical information based on the user's query."
        
        "You are a helpful medical assistant. Provide concise and accurate medical information "
        "based on the user's query. Disclaimer: This information is for educational purposes only and is not a substitute for professional advice.\n\n"
        f"Question: {message.content}"
    )
    # Send the prompt to the Gemini model (using non-streaming mode for simplicity)
    response = chat.send_message(prompt, stream=False)
    answer = response.text if response and hasattr(response, "text") else "Sorry, I could not generate a response."
    # Send the generated response back to the user via Chainlit
    await cl.Message(content=answer).send()