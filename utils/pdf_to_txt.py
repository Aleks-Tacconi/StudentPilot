import PyPDF2

def convert_pdf(path: str) -> str:
    string_builder = ""

    with open(path, mode="rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)

        for _, page in enumerate(pdf_reader.pages):
            string_builder += page.extract_text()

    return string_builder
