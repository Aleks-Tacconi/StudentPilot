import streamlit as st
import time
import os
from openai import OpenAI

# Ensure your API key is set correctly


class StudyTimer:
    def __init__(self):
        self.study_time = 25  # Default value in minutes
        self.total_seconds = self.study_time * 60

    def get_user_input(self):
        self.study_time = st.slider("Set study time (minutes):", min_value=1, max_value=120, value=25)
        self.total_seconds = self.study_time * 60

    def generate_quote(self):
        key = os.getenv("OPENAI_API_KEY")
        gpt = OpenAI(api_key=key)
        try:
            # Send the request to the Chat API for a motivational quote
            response = gpt.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant"
                    },
                    {
                        "role": "user",
                        "content": "Create a motivational quote in the format: 'quote - author'"
                    }
                ]
            )

            question = response.choices[0].message.content
            return question
        except Exception as e:
            st.error(f"Error generating quote: {e}")
            return "Keep going, you're doing great! 💪"

    def start_timer(self):

        if st.button("Start Timer"):
            st.write(f"⏳ Timer started for {self.study_time} minutes!")

            progress_bar = st.progress(0)
            countdown_text = st.empty()
            quote_text = st.empty()

            for remaining in range(self.total_seconds, -1, -1):
                mins, secs = divmod(remaining, 60)
                countdown_text.write(f"Time left: {mins:02d}:{secs:02d}")
                progress_bar.progress((self.total_seconds - remaining) / self.total_seconds)

                if remaining % 60 == 0 and remaining != self.total_seconds:
                    quote = self.generate_quote()
                    quote_text.write(f"💬 {quote}")

                time.sleep(1)  # Sleep for 1 second

            st.success("✅ Time's up! Take a break! 🎉")

    def run(self):
        st.title("📚 Study Timer")
        self.get_user_input()
        self.start_timer()


# Instantiate and run the timer
if __name__ == "__main__":
    timer = StudyTimer()
    timer.run()
