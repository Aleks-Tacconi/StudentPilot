from utils import generate_question_answer
import os


def main() -> None:
    qna = {}

    with open(os.path.join("uploaded_files", "questions.txt"), mode="r", encoding="utf-8") as f:
        for note in f.readlines():
            note = note.strip()
            question, answer = generate_question_answer(note)

            qna[question] = answer


    with open("qna.txt", mode="w", encoding="utf-8") as f:
        for question, answer in qna.items():
            f.write(f"{question.strip()}%%%%%{answer.strip()}\n")


if __name__ == "__main__":
    main()
