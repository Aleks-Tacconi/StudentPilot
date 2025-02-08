import streamlit as st

from components import StFlashCard
from components import FlashCard

from components import CardNavigation
from components import Quote

from pages import UploadFile


def gen_flashcards() -> None:
    with open("qna.txt", mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            try:
                question, answer = line.strip().split("%%%%%")
                if question != "Error":
                    flash_card = FlashCard(question, answer)
                    StFlashCard(flash_card)
            except Exception:
                pass


class Application:
    def __init__(self) -> None:
        self.__previous_flash_card = CardNavigation(-1, "<")
        self.__next_flash_card = CardNavigation(1, "\>")
        self.__quote = Quote()

        self.__upload_page = UploadFile()

        if "button_index" not in st.session_state:
            st.session_state.button_index = 0

        if "left_arrow" not in st.session_state:
            st.session_state.left_arrow = False

        if "right_arrow" not in st.session_state:
            st.session_state.right_arrow = True

        if "page" not in st.session_state:
            st.session_state.page = "page_1"

        self.__current_button_label = None

    def page_1(self) -> None:
        self.__upload_page.render()
        self.__upload_page.upload_txt()

    def page_2(self) -> None:
        gen_flashcards()

        button = list(StFlashCard.all.values())[st.session_state.button_index]
        self.__current_button_label = button.button_label()

        left, _, middle, _, right = st.columns([1, 1, 8, 1, 1])

        StFlashCard.all[self.__current_button_label].render(middle)

        if st.session_state.left_arrow:
            self.__previous_flash_card.render(left)
        if st.session_state.right_arrow:
            self.__next_flash_card.render(right)

        total_flashcards = len(StFlashCard.all)
        progress = (st.session_state.button_index + 1) / total_flashcards
        st.progress(progress)

        st.markdown("---")

        self.__quote.render()

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
