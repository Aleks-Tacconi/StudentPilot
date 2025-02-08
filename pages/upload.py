import streamlit as st
import os


class UploadFile:
    def __init__(self) -> None:
        self.uploaded_dir = "uploaded_files"
        self.file_path = None
        self.flash_cards = []

    def render(self) -> None:
        st.title("AI-Powered Flash Cards!")
        st.write("Our AI-powered flashcards automatically create personalized question-and-answer cards from your notes, helping you focus on key concepts for more effective revision. Tailored to your material, they offer a smart, dynamic way to study, making your revision faster, easier, and more efficient.")
        st.markdown("---")
        st.html("<h2>Upload Your File 📂</h2>")
        st.write(
            "Welcome to trash revision. Please upload a file so we can make some flash cards."
        )

    def upload_txt(self) -> None:
        uploaded_file = st.file_uploader("Choose a file", type=["txt"])

        if uploaded_file is not None:
            st.success("File uploaded successfully! Generating Flash Cards...")
            self.save_uploaded_file(uploaded_file)
            self.create_flashcards()

    def save_uploaded_file(self, uploaded_file) -> None:
        os.makedirs(self.uploaded_dir, exist_ok=True)

        self.file_path = os.path.join(self.uploaded_dir, "questions.txt")

        with open(self.file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    def create_flashcards(self) -> None:
        os.system("python gen_qna.py")
        self.switch_to_status()

    def switch_to_status(self) -> None:
        st.write("Navigating to Status Page...")
        st.session_state.page = "page_2"
        st.rerun()
