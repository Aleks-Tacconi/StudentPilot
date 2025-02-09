from utils import generate_question_answer
import os


def main() -> None:
    path = os.path.join("uploaded_files", "questions.txt")
    with open(path, mode="r", encoding="utf-8") as f:
        note = "".join(f.readlines())
        response = generate_question_answer(note)

    with open("qna.txt", mode="w", encoding="utf-8") as f:
        for line in response.split("\n"):
            if line.strip() != "":
                f.write(line + "\n")


if __name__ == "__main__":
    main()
