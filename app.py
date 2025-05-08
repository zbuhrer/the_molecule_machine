import streamlit as st
from modules import atomic_viewer, periodic_table, reaction_simulator, math_workbench, lessons
import config

# App configuration
st.set_page_config(
    page_title=config.APP_NAME,
    page_icon=config.APP_ICON,
    layout=config.DEFAULT_LAYOUT,
    initial_sidebar_state=config.INITIAL_SIDEBAR_STATE,
)

# App title
st.title("The Molecule Machine")

# Sidebar (Navigation)
with st.sidebar:
    st.header("Modules")
    selected_module = st.selectbox("Select a module:", ["Welcome", "Atomic Viewer", "Periodic Table", "Reaction Simulator", "Math Workbench", "Lessons"])

# Main content area (Module display)
if selected_module == "Welcome":
    st.write(f"Welcome to {config.APP_NAME}!")
    st.write("Select a module from the sidebar to get started.")
elif selected_module == "Atomic Viewer":
    atomic_viewer.render()
elif selected_module == "Periodic Table":
    periodic_table.render()
elif selected_module == "Reaction Simulator":
    reaction_simulator.render()
elif selected_module == "Math Workbench":
    math_workbench.render()
elif selected_module == "Lessons":
    lessons.render()
