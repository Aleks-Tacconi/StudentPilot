from openai import OpenAI
import streamlit as st

import os
file = st.file_uploader("Choose a file", type=["txt"])
if file is not None:
    
    file_content = file.read().decode("utf-8") 

st.title("ChatGPT-like clone")

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini-2024-07-18"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter you queries here?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[

        
                {
                    "role": m["role"], 
                    "content": m["content"] + file_content
                }
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})