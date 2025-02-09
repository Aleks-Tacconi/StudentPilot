from abc import ABCMeta, abstractmethod

import streamlit as st

class Page(metaclass=ABCMeta):
    @abstractmethod
    def render(self) -> None: ...

    def sep(self) -> None:
        st.html("""
            <style>
                hr {
                    width: 100%;  /* Make the line span the entire width */
                    border: 1px solid white;  /* You can adjust the color and style of the line */
                    margin: -10;  /* Optional: to remove any margin around the line */
                }
            </style>
            <hr>
        """)
