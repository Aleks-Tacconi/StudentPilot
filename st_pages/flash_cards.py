import os
import streamlit as st

from utils import read_file

from components import StFlashCard
from components import CardNavigation
from .page import Page


class FlashCardsPage(Page):
    def __init__(self) -> None:
        self.__previous_flash_card = CardNavigation(-1, "&lt;")
        self.__next_flash_card = CardNavigation(1, "&gt;")

        if "button_index" not in st.session_state:
            st.session_state.button_index = 0

        if "left_arrow" not in st.session_state:
            st.session_state.left_arrow = False

        if "right_arrow" not in st.session_state:
            st.session_state.right_arrow = True

        self.__current_button_label = None
        self.__notes = read_file(os.path.join("db", "notes.md"))

    def render(self) -> None:

        st.title("Flash Cards")
        self.sep()
        st.html("<br>")

        button = list(StFlashCard.all.values())[st.session_state.button_index]
        self.__current_button_label = button.button_label()

        left, _, middle, _, right = st.columns([1, 0.2, 8, 0.2, 1])

        StFlashCard.all[self.__current_button_label].render(middle)

        if st.session_state.left_arrow:
            self.__previous_flash_card.render(left)
        if st.session_state.right_arrow:
            self.__next_flash_card.render(right)

        total_flashcards = len(StFlashCard.all)
        progress = (st.session_state.button_index + 1) / total_flashcards
        st.progress(progress)

        st.html("<br>")

        st.title("Study Resources")
        self.sep()
        st.markdown(self.__notes)

        st.sidebar.markdown(" ")
        st.sidebar.html(
            "<h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Previous Flash Cards</h1>"
        )
        st.sidebar.markdown("---")
        for i in range(st.session_state.button_index):
            button = list(StFlashCard.all.values())[i]
            button_label = button.button_label()
            args = StFlashCard.all[button_label].button_args()
            st.sidebar.button(
                args[0].replace("250", "150"), on_click=args[1], type="tertiary"
            )
