import os

from utils import generate_question_answer
from utils import generate_summmarised_notes

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
    gen_flash_cards()
    gen_notes()

if __name__ == "__main__":
    main()
