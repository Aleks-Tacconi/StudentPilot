import streamlit as st
import os
from openai import OpenAI


def generate_question_answer(note: str) -> str:
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
                    + "generate 10 questions from the above content in the form {question}%%%%%{answer}",
                },
            ],
        )
        return response.choices[0].message.content

    except Exception as e:
        st.error(f"Error generating: {e}")
        return "Error"


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
