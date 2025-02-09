import os

import streamlit as st

from components import StFlashCard
from components import FlashCard

from st_pages import UploadPage
from st_pages import FlashCardsPage


def gen_flashcards() -> None:
    with open(os.path.join("db", "qna.txt"), mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            try:
                question, answer = line.strip().split("%%%%%")

                dot_index = question.find(".")
                question = question[dot_index + 2:]

                if question.endswith("."):
                    question = question[: len(question) - 1]
                if answer.endswith("."):
                    answer = answer[: len(answer) - 1]

                if question.endswith("}"):
                    question = question[: len(question) - 1]
                if answer.endswith("}"):
                    answer = answer[: len(answer) - 1]

                if question.startswith("{"):
                    question = question[1:]
                if answer.startswith("{"):
                    answer = answer[1:]

                question = question.replace("`", "")
                answer = answer.replace("`", "")

                if question != "Error":
                    flash_card = FlashCard(question, answer)
                    StFlashCard(flash_card)
            except ValueError:
                pass

    if not StFlashCard.all:
        flash_card = FlashCard(" ", " ")
        StFlashCard(flash_card)


class Application:
    def __init__(self) -> None:
        self.__upload_page = UploadPage()
        self.__flash_cards_page = FlashCardsPage()

        if "page" not in st.session_state:
            st.session_state.page = "page_1"

    def page_1(self) -> None:
        self.__upload_page.render()

    def page_2(self) -> None:
        gen_flashcards()
        self.__flash_cards_page.render()

    def main(self) -> None:
        if st.session_state.page == "page_1":
            self.page_1()
        elif st.session_state.page == "page_2":
            self.page_2()


def main() -> None:
    app = Application()
    app.main()


if __name__ == "__main__":
    main()
