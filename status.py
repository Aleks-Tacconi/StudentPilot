import streamlit as st
import pandas as pd


# Class to handle the results of the ocean finds
class Results:
    def __init__(self) -> None:
        # Initialize ocean finds with trash and treasure data
        self.ocean_finds = {
            "trash": {
                "Plastic Bottles": {"amount": 5, "times_found": 3},
                "Fishing Nets": {"amount": 2, "times_found": 2},
                "Metal Cans": {"amount": 3, "times_found": 1},
                "Rubber Tires": {"amount": 1, "times_found": 1},
                "Glass Bottles": {"amount": 4, "times_found": 2}
            },
            "treasure": {
                "Gold Coins": {"amount": 10, "times_found": 4},
                "Silver Bars": {"amount": 2, "times_found": 1},
                "Pearls": {"amount": 5, "times_found": 3},
                "Ancient Artifacts": {"amount": 1, "times_found": 1},
                "Jewelry": {"amount": 3, "times_found": 2}
            }
        }

        # Initialize a dataframe to hold results
        self.__data_frame = pd.DataFrame(
            {
                "Item": ["Plastic Bottles", "Fishing Nets", "Metal Cans", "Rubber Tires", "Glass Bottles", "Gold Coins",
                         "Silver Bars", "Pearls", "Ancient Artifacts", "Jewelry"],
                "Amount Found": [5, 2, 3, 1, 4, 10, 2, 5, 1, 3],
                "Times Found": [3, 2, 1, 1, 2, 4, 1, 3, 1, 2]
            }
        )

    def total_found(self):
        # Calculate the total amount of trash and treasure
        total_trash_amount = sum(item["amount"] for item in self.ocean_finds["trash"].values())
        total_treasure_amount = sum(item["amount"] for item in self.ocean_finds["treasure"].values())

        return total_trash_amount, total_treasure_amount

    def display_results(self):
        # Get the total trash and treasure amounts
        total_trash, total_treasure = self.total_found()

        # Use Streamlit to display the results
        st.title("Status Page")
        st.text("You have finished 10 flash cards in 5 minutes.")

        st.text(f"Here is the trash you collected: {total_trash} items.")
        st.text(f"Here is the treasure you collected: {total_treasure} items.")

        st.text("Detailed Collection:")
        st.write(self.__data_frame)


# Create an instance of Results
results = Results()

# Display the results
results.display_results()
