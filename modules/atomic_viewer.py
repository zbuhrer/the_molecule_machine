import streamlit as st
from components.molecule_renderer import render_3d_molecule
from utils.data_loader import load_periodic_table
from logging_config import logger

def render():
    logger.info("Atomic Viewer render function called.")
    st.header("Atomic Viewer")

    # Load periodic table data (for element selection)
    try:
        logger.debug("Attempting to load periodic table data.")
        periodic_table = load_periodic_table()
        elements = list(periodic_table.keys())
        logger.debug(f"Periodic table loaded successfully. Elements: {elements}")
    except FileNotFoundError as e:
        logger.error("Error loading periodic table data.")
        logger.exception(e)  # Log the full exception, including traceback
        st.error("Error: Could not load periodic table data. Make sure periodic_table.json exists in the data directory.")
        return

    # Element selection
    selected_element = st.selectbox("Select an element:", elements)
    logger.debug(f"User selected element: {selected_element}")

    # Display element information (from periodic table)
    if selected_element:
        element_data = periodic_table.get(selected_element)
        if element_data:
            st.subheader(f"{selected_element} - {element_data.get('name', '')}")
            st.write(f"Atomic Number: {element_data.get('atomic_number', '')}")
            st.write(f"Atomic Mass: {element_data.get('atomic_mass', '')}")
            st.write(f"Electron Configuration: {element_data.get('electron_configuration', '')}")

            st.subheader("3D Atom Visualization")
            render_3d_molecule(element=selected_element)
            logger.debug(f"Rendered 3D molecule for element: {selected_element}")

        else:
            st.warning(f"No data found for {selected_element} in the periodic table.")
            logger.warning(f"No data found for element {selected_element} in periodic table.")
