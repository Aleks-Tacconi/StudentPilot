import streamlit as st
import pandas as pd
import os

# with open('style.css') as file:
#     css = file.read()
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

class Upload_file:
    def __init__(self):
        self.uploaded_dir = "../uploaded_files"
        self.file_path = None
        self.flash_cards = []

    def title(self):
        st.title("Upload Your File 📂")
        st.write ("Welcome to trash revision please upload a file so we can make some flash cards")

    def upload_txt(self):
        uploaded_file = st.file_uploader("Choose a file", type=["txt"])
        #
        # # Check if a file is uploaded
        # if uploaded_file is not None:
        #     st.success("Please select a file")
        #     return None
        #
        # # Handling CSV files
        # elif uploaded_file.name.endswith(".txt"):
        #     # content = uploaded_file.read().decode("utf-8")
        #     # st.write("📄 File Content:")
        #     # st.text(content)
        #     self.save_uploaded_file(uploaded_file)
        #     self.read_file.content(uploaded_file)
        #     st.success("File uploaded Successfully")
        #
        # else:
        #     st.success("Please upload a txt. file")
        #     return None

        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            self.save_uploaded_file(uploaded_file)
            self.read_file_content(uploaded_file)
            return uploaded_file
        return None

    def save_uploaded_file(self,uploaded_file):
         # Create a directory to save the uploaded file
        upload_dir = "uploaded_files"
        os.makedirs(upload_dir, exist_ok=True)

        # Define the path where the file will be saved
        self.file_path = os.path.join(upload_dir, uploaded_file.name)

        # Write the uploaded file to the local directory
        with open(self.file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the path of the saved file
        st.write(f"File saved at: {self.file_path}")

    def read_file_content(self,uploaded_file):
        content = uploaded_file.read().decode("utf-8")
        st.write("📄 File Content:")
        st.text(content)
        self.create_flashcards(content)

    def create_flashcards(self,content):
        # Example: Create flashcards by splitting lines (if applicable)
        self.flashcards = content.split('\n')
        self.flashcards = [line.split('-') for line in self.flashcards if '-' in line]
        if self.flashcards:
            flashcards_df = pd.DataFrame(self.flashcards, columns=['Question', 'Answer'])
            # st.write("📝 Flashcards Preview:")
            # st.dataframe(flashcards_df)
            if st.button("See flashcards➡️"):
                # page is where the upload.py is
                # going there and displaying that file
                #st.switch_page("status")
                st.button("Go to Status Page", on_click=self.switch_to_status)
        else:
            st.warning("No flashcards could be generated from the text file.")

        def switch_to_status(self):
            # This method will be triggered when the button is clicked
            st.switch_page("status")


app = Upload_file()
app.title()
uploaded_txt = app.upload_txt()
