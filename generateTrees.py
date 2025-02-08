import streamlit as st
import os
from openai import OpenAI

class Trash:
    def __init__(self):
        self.item_name = ""
        self.value = ""


    def write(self):
        loading_placeholder = st.empty()
        content_placeholder = st.empty()

        loading_placeholder.write("Generating tree...")

        response = self.generate_trash()
        content_placeholder.write(response)


    def generate_trash(self):
        key = os.getenv("OPENAI_API_KEY")
        gpt = OpenAI(api_key=key)
        try:
            response = gpt.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant"
                    },
                    {
                        "role": "user",
                        "content": "Write a random tree type such as oak. One one word"
                    }
                ]
            )
            response_content = response.choices[0].message.content
            return response_content
        except Exception as e:
            st.error(f"Error generating item and value: {e}")
            return "Error"


    def generate_image(self, item_name):
        key = os.getenv("OPENAI_API_KEY")
        gpt = OpenAI(api_key=key)
        try:
            response = gpt.images.generate(
                model="dall-e-3",
                prompt=f"A realistic image of {item_name} found in the ocean.",
                size="1024x1024",
                quality="standard"
            )
            return response.data[0].url
        except Exception as e:
            st.error(f"Error generating image: {e}")
            return None

if __name__ == "__main__":
    trash = Trash()
    trash.write()
