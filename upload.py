

import streamlit as st
import pandas as pd
import os

# Uncomment if you're applying custom CSS
# with open('style.css') as file:
#     css = file.read()
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

class Upload_file:
    def __init__(self):
        self.uploaded_dir = "uploaded_files"
        self.file_path = None
        self.flash_cards = []

    def title(self):
        st.title("Upload Your File 📂")
        st.write("Welcome to trash revision. Please upload a file so we can make some flash cards.")

    def upload_txt(self):
        uploaded_file = st.file_uploader("Choose a file", type=["txt"])

        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            self.save_uploaded_file(uploaded_file)
            self.read_file_content(uploaded_file)
            return uploaded_file
        return None

    def save_uploaded_file(self, uploaded_file):
        # Create a directory to save the uploaded file
        os.makedirs(self.uploaded_dir, exist_ok=True)

        # Define the path where the file will be saved
        self.file_path = os.path.join(self.uploaded_dir, uploaded_file.name)

        # Write the uploaded file to the local directory
        with open(self.file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the path of the saved file
        st.write(f"File saved at: {self.file_path}")

    def read_file_content(self, uploaded_file):
        content = uploaded_file.read().decode("utf-8")
        st.write("📄 File Content:")
        st.text(content)
        self.create_flashcards(content)

    def create_flashcards(self, content):
        # Split content by lines
        lines = content.split('\n')

        # Initialize flashcards list
        self.flashcards = []

        # Each line is a question, and we provide an empty answer or placeholder
        for line in lines:
            question = line.strip()

            # If the question is not empty, add it as a flashcard with no answer
            if question:
                self.flashcards.append([question, "No answer available"])

        # Check if flashcards were created
        if self.flashcards:
            flashcards_df = pd.DataFrame(self.flashcards, columns=['Question', 'Answer'])
            st.write("📝 Flashcards Preview:")
            st.dataframe(flashcards_df)

            # Add a button to navigate to the status page (this requires a page called "status")
            if st.button("See Status ➡️"):
                self.switch_to_status()
        else:
            st.warning("No flashcards could be generated from the text file.")

    def switch_to_status(self):
        # This method will be triggered when the button is clicked
        st.write("Navigating to Status Page...")
        # Ensure you've configured pages in Streamlit to use `st.switch_page()`
        st.switch_page("status")  # Ensure this page exists

# Initialize and run the app
app = Upload_file()
app.title()
uploaded_txt = app.upload_txt()
