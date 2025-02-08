import time
import os

import streamlit as st
from openai import OpenAI

from utils import generate_quote


class StudyTimer:
    def __init__(self):
        if "study_time" not in st.session_state:
            st.session_state.study_time = 25

        if "total_seconds" not in st.session_state:
            st.session_state.total_seconds = st.session_state.study_time * 60

        if "timer_started" not in st.session_state:
            st.session_state.timer_started = False

        if "counter" not in st.session_state:
            st.session_state.counter = -1

        if "quote" not in st.session_state:
            st.session_state.quote = ""

    def on_click(self) -> None:
        st.session_state.timer_started = True

    def get_user_input(self):
        if not st.session_state.timer_started:
            st.session_state.study_time = st.slider(
                "Set study time (minutes):", min_value=1, max_value=120, value=25
            )
            st.session_state.total_seconds = st.session_state.study_time * 60

    def start_timer(self):
        if st.session_state.timer_started:
            st.write(f"⏳ Timer started for {st.session_state.study_time} minutes!")

            progress_bar = st.progress(0)
            countdown_text = st.empty()

            if st.session_state.quote == "":
                quote_text = st.empty()
            else:
                quote_text = st.empty()
                quote_text.write(st.session_state.quote)

            if st.session_state.counter == -1:
                upper = st.session_state.total_seconds
            else:
                upper = st.session_state.counter


            for remaining in range(upper, -1, -1):
                st.session_state.counter = remaining
                mins, secs = divmod(remaining, 60)
                countdown_text.write(f"Time left: {mins:02d}:{secs:02d}")
                progress_bar.progress(
                    (st.session_state.total_seconds - remaining) / st.session_state.total_seconds
                )

                if remaining % 60 == 0:
                    st.session_state.quote = generate_quote()
                    quote_text.write(st.session_state.quote)

                time.sleep(1)

            st.success("✅ Time's up! Take a break! 🎉")
            st.session_state.counter = -1

    def render(self) -> None:
        if not st.session_state.timer_started:
            st.button("Start Timer", type="secondary", on_click=self.on_click)

    def run(self) -> None:
        st.markdown(
            "<h1 style='text-align: center;'>📚 Study Timer</h1>",
            unsafe_allow_html=True,
        )
        self.get_user_input()
        self.start_timer()
