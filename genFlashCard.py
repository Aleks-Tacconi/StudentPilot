import streamlit as st
import os
from openai import OpenAI


class FlashCard:
    def __init__(self):
        self.question = ""
        self.answer = ""

    def write(self):
        question_placeholder = st.empty()
        answer_placeholder = st.empty()

        notes = "What is the power house of the cell?"
        response = self.generate_question_answer(notes)

        # Check if the response is in the expected format
        if response != "Error":
            question_placeholder.write(f"**Question:** {response[0]}")
            answer_placeholder.write(f"**Answer:** {response[1]}")
        else:
            st.error("Failed to generate the question and answer.")

    def generate_question_answer(self, notes):
        key = os.getenv("OPENAI_API_KEY")
        gpt = OpenAI(api_key=key)
        try:
            response = gpt.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful revision assistant."
                    },
                    {
                        "role": "user",
                        "content": notes + " In the format of Q: <question> A: <answer>"
                    }
                ]
            )
            response_content = response.choices[0].message.content

            if "Q:" in response_content and "A:" in response_content:
                question_start = response_content.find("Q:") + len("Q:")
                answer_start = response_content.find("A:") + len("A:")
                question = response_content[question_start:answer_start - len("A:")].strip()
                answer = response_content[answer_start:].strip()

                self.question = question
                self.answer = answer
                return self.question, self.answer
        except Exception as e:
            st.error(f"Error generating: {e}")
            return "Error"


if __name__ == "__main__":
    flash_card = FlashCard()
    flash_card.write()
