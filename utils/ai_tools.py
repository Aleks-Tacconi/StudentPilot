import streamlit as st
import os
from openai import OpenAI


def generate_question_answer(note: str) -> tuple:
    print("API CALL")
    key = os.getenv("OPENAI_API_KEY")
    gpt = OpenAI(api_key=key)

    try:
        response = gpt.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "You are a helpful revision assistant."},
                {
                    "role": "user",
                    "content": note
                    + " In the format of Q: <question> A: <answer> Short answers only",
                },
            ],
        )
        response_content = response.choices[0].message.content

        if "Q:" in response_content and "A:" in response_content:
            question_start = response_content.find("Q:") + len("Q:")
            answer_start = response_content.find("A:") + len("A:")
            question = response_content[
                question_start : answer_start - len("A:")
            ].strip()
            answer = response_content[answer_start:].strip()

            return question, answer
        return "Error", "Error"
    except Exception as e:
        st.error(f"Error generating: {e}")
        return "Error", "Error"


def generate_quote():
    key = os.getenv("OPENAI_API_KEY")
    gpt = OpenAI(api_key=key)
    try:
        response = gpt.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {
                    "role": "user",
                    "content": "Create a random motivational quote in the format: 'quote - author'",
                },
            ],
        )

        question = response.choices[0].message.content
        return question
    except Exception as e:
        st.error(f"Error generating quote: {e}")
        return "Keep going, you're doing great! 💪"
