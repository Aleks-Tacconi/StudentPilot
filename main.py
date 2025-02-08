import streamlit as st
import pandas as pd
import time

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

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

import streamlit as st
import time

# Title
st.title("📚 Study Timer")

# User input for timer duration
study_time = st.slider("Set study time (minutes):", min_value=1, max_value=120, value=1)

# Convert to seconds
total_seconds = study_time * 60

# Start button

