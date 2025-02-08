import streamlit as st

# Load and apply CSS
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- Opening Page ----
st.markdown("<h1 class='title'>📚 Welcome to Trash Revision</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Turn your notes into interactive flashcards with AI-powered generation!</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>And clean up the ocean!</p>", unsafe_allow_html=True)



if st.button("Get Started ➡️"):
    # page is where the upload.py is
    # going there and displaying that file
    st.switch_page("upload")


if st.button("See Status ➡️"):
    # page is where the upload.py is
    # going there and displaying that file
    st.switch_page("status")