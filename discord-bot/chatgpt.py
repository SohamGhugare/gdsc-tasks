import openai
from dotenv import load_dotenv
load_dotenv(".env")
import os
from typing import List

# Setting the api key
openai.api_key = os.getenv("API_KEY")

class ChatGPT:
    """
        CHATGPT
        This class contains all the methods for connecting to the ChatGPT API and fetching the responses
    """
    def __init__(self):
        # Setting an entry point for the API
        self.messages = [
            {
                "role": "system", 
                "content": "You are an intelligent assistant."
            }
        ]

    def get_response(self, message: str) -> str:
        self.messages.append({
            "role": "user",
            "content": message
        })
        # Fetching response wrt the history
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        ).choices[0].message.content
        self.messages.append({
            "role": "assistant",
            "content": res
        })
        return res

# Dummy driver code
if __name__ == "__main__":
    chatgpt = ChatGPT()
    while True:
        res = chatgpt.get_response(input("User: "))
        print(f"ChatGPT: {res}")
