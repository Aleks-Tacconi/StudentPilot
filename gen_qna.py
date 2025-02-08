from utils import generate_question_answer
import os


def main() -> None:
    with open(os.path.join("uploaded_files", "questions.txt"), mode="r", encoding="utf-8") as f:
        note = "".join(f.readlines())
        response = generate_question_answer(note)


    with open("qna.txt", mode="w", encoding="utf-8") as f:
        f.write(response)


if __name__ == "__main__":
    main()
