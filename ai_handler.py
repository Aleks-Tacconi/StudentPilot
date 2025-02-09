import os

from utils import generate_question_answer
from utils import generate_summmarised_notes
from utils import convert_pdf

def handle_other_formats() -> None:
    file = os.listdir("uploaded_files")[0]

    if file.endswith("pdf"):
        string = convert_pdf(os.path.join("uploaded_files", file))

        with open(os.path.join("uploaded_files", "questions.txt"), mode="w+", encoding="utf-8") as f:
            f.write(string)


def gen_flash_cards() -> None:
    path = os.path.join("uploaded_files", "questions.txt")
    with open(path, mode="r", encoding="utf-8") as f:
        note = "".join(f.readlines())
        response = generate_question_answer(note)

    with open(os.path.join("db", "qna.txt"), mode="w", encoding="utf-8") as f:
        for line in response.split("\n"):
            if line.strip() != "":
                f.write(line + "\n")

def gen_notes() -> None:
    path = os.path.join("uploaded_files", "questions.txt")

    with open(path, mode="r", encoding="utf-8") as f:
        note = "".join(f.readlines())
        response = generate_summmarised_notes(note)

    with open(os.path.join("db", "notes.md"), mode="w", encoding="utf-8") as f:
        f.write(response)


def main() -> None:
    handle_other_formats()
    gen_flash_cards()
    gen_notes()

if __name__ == "__main__":
    main()
