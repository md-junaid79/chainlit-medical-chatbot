# app.py
import chainlit as cl
import os
from dotenv import load_dotenv
import google.generativeai as genai
from chainlit import AskUserMessage, Message, on_chat_start

# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    raise Exception("Gemini API key not found. Please set GOOGLE_API_KEY in your .env file.")

# Configure Gemini API with your key
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

# @cl.on_chat_start
# async def start():
#     await cl.Message(content="""Hello and welcome to your Confidential Medical Chatbot.

# I'm designed to be a private and helpful space to explore your medical questions and concerns.  Your privacy is important.

# **Please be aware:**  This chatbot is an AI tool for information and should **not replace consultations with your medical provider.**  They are essential for your personal healthcare.

# I can help you understand medical topics, explore symptoms (for informational purposes), and find resources.  What medical questions can I help you with in a confidential manner today?""").send()

@cl.on_message
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