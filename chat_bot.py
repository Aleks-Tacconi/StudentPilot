from openai import OpenAI
import streamlit as st

import os

file = st.file_uploader("Choose a file", type=["txt"])

if file is not None:
    file_content = file.read().decode("utf-8")

