import streamlit as st

st.title("Collection")

# Initialize session state for collected trees
if "collected_trees" not in st.session_state:
    st.session_state.collected_trees = []

# Function to display collected trees
def display_collected_trees():
    st.write("### Collected Trees")
    if st.session_state.collected_trees:
        for tree in st.session_state.collected_trees:
            st.write(f"- {tree}")
    else:
        st.write("No trees collected yet.")

# Function to reset collected trees
def reset_trees():
    st.session_state.collected_trees = []
    st.success("Tree collection reset!")

# Button to simulate tree generation
if st.button("Generate Tree"):
    # This is just a mock for tree generation, you can replace it with your actual tree generator logic
    new_tree = "Oak"  # Example tree, replace with your generation logic
    st.session_state.collected_trees.append(new_tree)  # Add tree to collection
    st.success(f"Generated and added tree: {new_tree}")

# Display collected trees
display_collected_trees()

# Button to reset collection
if st.button("Reset Tree Collection"):
    reset_trees()
