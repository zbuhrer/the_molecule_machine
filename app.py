import streamlit as st
from modules import atomic_viewer, periodic_table, reaction_simulator, math_workbench, lessons
import config
from logging_config import logger

# App configuration
st.set_page_config(
    page_title=config.APP_NAME,
    page_icon=config.APP_ICON,
    layout=config.DEFAULT_LAYOUT,
    initial_sidebar_state=config.INITIAL_SIDEBAR_STATE,
)

# App title
st.title("The Molecule Machine")
logger.info("Application started.")

# Sidebar (Navigation) - Now just a simplified version
# with st.sidebar:
#     st.header("Modules")
#     selected_module = st.selectbox("Select a module:", ["Welcome", "Atomic Viewer", "Periodic Table", "Reaction Simulator", "Math Workbench", "Lessons"])


# Tabbed Interface - New Implementation
tab_names = ["Welcome", "Atomic Viewer", "Periodic Table", "Reaction Simulator", "Math Workbench", "Lessons"]
tabs = st.tabs(tab_names)  # Creates the tabs

# Main content area (Module display) - Now using tabs
with tabs[0]:  # Welcome tab
    st.write(f"Welcome to {config.APP_NAME}!")
    st.write("Select a module from the tabs above to get started.")
    logger.debug("Welcome tab displayed.")

with tabs[1]:  # Atomic Viewer tab
    logger.info("Atomic Viewer tab selected.")
    atomic_viewer.render()

with tabs[2]:  # Periodic Table tab
    logger.info("Periodic Table tab selected.")
    periodic_table.render()

with tabs[3]:  # Reaction Simulator tab
    logger.info("Reaction Simulator tab selected.")
    reaction_simulator.render()

with tabs[4]:  # Math Workbench tab
    logger.info("Math Workbench tab selected.")
    math_workbench.render()

with tabs[5]:  # Lessons tab
    logger.info("Lessons tab selected.")
    lessons.render()
