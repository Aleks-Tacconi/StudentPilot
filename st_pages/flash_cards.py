import streamlit as st

from components import StFlashCard
from components import CardNavigation
from .page import Page


class FlashCardsPage(Page):
    def __init__(self) -> None:
        self.__previous_flash_card = CardNavigation(-1, "<")
        self.__next_flash_card = CardNavigation(1, "\>")

        if "button_index" not in st.session_state:
            st.session_state.button_index = 0

        if "left_arrow" not in st.session_state:
            st.session_state.left_arrow = False

        if "right_arrow" not in st.session_state:
            st.session_state.right_arrow = True

        self.__current_button_label = None

    def render(self) -> None:
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
