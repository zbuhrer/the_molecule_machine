import streamlit as st
from utils.data_loader import load_lessons_markdown


def render():
    st.header("Lessons and Tutorials")

    lessons_data = load_lessons_markdown()

    if lessons_data:
        # Display the lessons using expanders
        for title, content in lessons_data.items():
            with st.expander(title):
                st.markdown(content, unsafe_allow_html=True)
    else:
        st.warning("No lessons found. Please make sure lessons.md exists in the data directory.")
