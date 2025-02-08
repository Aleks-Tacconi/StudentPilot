import streamlit as st
from utils import generate_quote


class Quote:
    def __init__(self) -> None:
        if "quote" not in st.session_state:
            st.session_state.quote = ""

    def change_quote(self) -> None:
        quote = generate_quote()
        st.session_state.quote = quote

    def render(self) -> None:
        st.button("Insire me", type="secondary", on_click=self.change_quote)
        st.write(st.session_state.quote)
