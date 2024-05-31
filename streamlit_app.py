import streamlit as st

def main():
    st.title("Phrase Editor and Sorter")

    # Initialize the session state for phrases if it doesn't exist
    if 'phrases' not in st.session_state:
        st.session_state.phrases = ["Example phrase 1", "Example phrase 2", "Example phrase 3"]

    st.subheader("Edit Phrases")
    phrases_text = "\n".join(st.session_state.phrases)
    updated_phrases_text = st.text_area("Enter phrases (one per line)", phrases_text, height=200)

    # Update the phrases list in session state
    st.session_state.phrases = updated_phrases_text.split("\n")

    # Button to sort phrases
    if st.button("Sort Phrases"):
        st.session_state.phrases = sorted(st.session_state.phrases)

    st.subheader("Current Phrases")
    st.write(st.session_state.phrases)

if __name__ == "__main__":
    main()
