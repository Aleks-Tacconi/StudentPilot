import streamlit as st
import pandas as pd
import os

# Uncomment if you're applying custom CSS
# with open('style.css') as file:
#     css = file.read()
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


class UploadFile:
    def __init__(self):
        self.uploaded_dir = "uploaded_files"
        self.file_path = None
        self.flash_cards = []

    def title(self):
        st.title("Upload Your File 📂")
        st.write(
            "Welcome to trash revision. Please upload a file so we can make some flash cards."
        )

    def upload_txt(self):
        uploaded_file = st.file_uploader("Choose a file", type=["txt"])

        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            self.save_uploaded_file(uploaded_file)
            self.read_file_content(uploaded_file)
            return uploaded_file
        return None

    def save_uploaded_file(self, uploaded_file):
        os.makedirs(self.uploaded_dir, exist_ok=True)

        self.file_path = os.path.join(self.uploaded_dir, "questions.txt")

        with open(self.file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    def read_file_content(self, uploaded_file):
        content = uploaded_file.read().decode("utf-8")
        st.write("📄 File Content:")
        self.create_flashcards(content)

    def create_flashcards(self, content):
        lines = content.split("\n")

        flashcards = []

        for line in lines:
            question = line.strip()

            if question:
                flashcards.append([question, "No answer available"])

        if flashcards:
            flashcards_df = pd.DataFrame(
                flashcards, columns=["Question", "Answer"]
            )
            st.write("📝 Flashcards Preview:")
            st.dataframe(flashcards_df)
            os.system("python gen_qna.py")

            if st.button("See Status ➡️"):
                self.switch_to_status()
        else:
            st.warning("No flashcards could be generated from the text file.")

    def switch_to_status(self):
        st.write("Navigating to Status Page...")
        st.session_state.page = "page_2"
        st.rerun()
