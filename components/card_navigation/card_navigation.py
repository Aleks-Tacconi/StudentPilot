import os
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from utils import read_css
from ..flash_card import StFlashCard


class CardNavigation:
    def __init__(self, direction: int, text: str) -> None:
        self.__direction = direction
        self.__text = text
        self.__css = read_css(
            os.path.join("components", "card_navigation", "card_navigation.css")
        )

    def __cycle(self) -> None:
        st.session_state.button_index = st.session_state.button_index + self.__direction

        if st.session_state.button_index > 0:
            st.session_state.left_arrow = True
        else:
            st.session_state.left_arrow = False

        if st.session_state.button_index < len(StFlashCard.all) - 1:
            st.session_state.right_arrow = True
        else:
            st.session_state.right_arrow = False

    def render(self, col: DeltaGenerator) -> None:
        st.markdown(self.__css, unsafe_allow_html=True)
        col.button(
            self.__text,
            on_click=self.__cycle,
            key=str(self.__direction),
            type="secondary",
        )
