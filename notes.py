def upload_txt(self):
        
        uploaded_file = st.file_uploader("Choose a file", type=["txt"])

        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            self.save_uploaded_file(uploaded_file)
            content = self.read_file_content(uploaded_file)  # Capture content

            # Proceed with OpenAI API call if content is not None
            if content:
                client = OpenAI(os.environ.get("OPENAI_API_KEY"))
                response = client.chat.completions.create(model="gpt-4o-mini-2024-07-18", messages=[
                    {"role": "system", "content": "You are a helpful assistant, generate summarised notes in markdown format"},
                    {"role": "user", "content": content},
                ])

                notes = response.choices[0].message.content
                st.title("Summarised Notes 📝")
                st.markdown(notes)
                

            return uploaded_file
        return None