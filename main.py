import streamlit as st

from components import StFlashCard
from components import FlashCard

from components import CardNavigation
from components import Quote


def gen_flashcards() -> None:
    with open("qna.txt", mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            question, answer = line.strip().split("%%%%%")
            flash_card = FlashCard(question, answer)
            StFlashCard(flash_card)


class Application:
    def __init__(self) -> None:
        self.__previous_flash_card = CardNavigation(-1, "<")
        self.__next_flash_card = CardNavigation(1, "\>")
        self.__quote = Quote()

        if "button_index" not in st.session_state:
            st.session_state.button_index = 0

        if "left_arrow" not in st.session_state:
            st.session_state.left_arrow = False

        if "right_arrow" not in st.session_state:
            st.session_state.right_arrow = True

        button = list(StFlashCard.all.values())[st.session_state.button_index]
        self.__current_button_label = button.button_label()

    def main(self) -> None:
        left, _, middle, _, right = st.columns([1, 1, 8, 1, 1])

        StFlashCard.all[self.__current_button_label].render(middle)

        if st.session_state.left_arrow:
            self.__previous_flash_card.render(left)
        if st.session_state.right_arrow:
            self.__next_flash_card.render(right)

        st.markdown("---")

        self.__quote.render()

def main() -> None:
    gen_flashcards()

    app = Application()
    app.main()


if __name__ == "__main__":
    main()
