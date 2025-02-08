import streamlit as st
import os
from openai import OpenAI

class Trash:
    def __init__(self):
        self.item_name = ""
        self.value = ""


    def write(self):
        loading_placeholder = st.empty()
        image_placeholder = st.empty()
        content_placeholder = st.empty()

        loading_placeholder.write("Retrieving trash from the ocean...")

        response = self.generate_trash()

        if response != "Error":
            self.item_name, self.value = response
            image_url = self.generate_image(self.item_name)

            if image_url:
                loading_placeholder.empty()
                content_placeholder.write(f"**Item:** {self.item_name}\n\n**Value:** {self.value}")
                image_placeholder.image(image_url)
                st.audio_input("soundFX/vine-booom.mp3", label_visibility="collapsed", autoplay=True)
            else:
                loading_placeholder.empty()
                st.error("Failed to generate image.")
        else:
            loading_placeholder.empty()
            st.error("Failed to generate the item and value.")

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
                        "content": "In the format of Item: <question> Value: <answer> , generate a random item and its "
                                   "associated value (can be guessed in £). These items must be things that can be "
                                   "randomly found in the ocean. Only generate 1 item. Also understate the estimated"
                                   "value by a massive amount."
                    }
                ]
            )
            response_content = response.choices[0].message.content

            if "Item:" in response_content and "Value:" in response_content:
                question_start = response_content.find("Item:") + len("Item:")
                answer_start = response_content.find("Value:") + len("Value:")
                question = response_content[question_start:answer_start - len("Value:")].strip()
                answer = response_content[answer_start:].strip()

                return question, answer
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
