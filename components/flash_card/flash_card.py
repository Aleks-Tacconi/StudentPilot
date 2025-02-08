from dataclasses import dataclass, field

import os
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from utils import read_css


@dataclass
class FlashCard:
    question: str
    answer: str
    difficulty_feedback: list = field(default_factory=list)


class StFlashCard:
    all = {}

    def __init__(self, flash_card: FlashCard) -> None:
        self.__flash_card = flash_card
        self.__flash_card_id = self.__flash_card.question
        self.__css = read_css(
            os.path.join("components", "flash_card", "flash_card.css")
        )

        self.__button_text = f"button_text_{self.__flash_card_id}"
        self.__is_question = f"is_question_{self.__flash_card_id}"

        if self.__button_text not in st.session_state:
            st.session_state[self.__button_text] = self.__flash_card.question
        if self.__is_question not in st.session_state:
            st.session_state[self.__is_question] = True

        StFlashCard.all[self.button_label()] = self

    def button_label(self) -> str:
        return self.__flash_card.question

    def __toggle(self) -> None:
        if st.session_state[self.__is_question]:
            st.session_state[self.__button_text] = self.__flash_card.answer
        else:
            st.session_state[self.__button_text] = self.__flash_card.question

        st.session_state[self.__is_question] = not st.session_state[self.__is_question]

    def render(self, col: DeltaGenerator) -> None:
        st.markdown(self.__css, unsafe_allow_html=True)
        col.button(
            st.session_state[self.__button_text], on_click=self.__toggle, type="primary"
        )
