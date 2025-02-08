import streamlit as st
import pandas as pd

class Application:
    def __init__(self) -> None:
        self.__data_frame = pd.DataFrame(
            {
                "first column": [1, 2, 3, 4],
                "second column": [10, 20, 30, 40]
            }
        )

    def main(self) -> None:
        st.write("my table:")
        st.write(self.__data_frame)

def main() -> None:
    app = Application()
    app.main()

if __name__ == "__main__":
    main()
