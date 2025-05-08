import streamlit as st
from components.molecule_renderer import render_3d_molecule
from utils.data_loader import load_periodic_table

def render():
    st.header("Atomic Viewer")

    # Load periodic table data (for element selection)
    try:
        periodic_table = load_periodic_table()
        elements = list(periodic_table.keys())
    except FileNotFoundError:
        st.error("Error: Could not load periodic table data. Make sure periodic_table.json exists in the data directory.")
        return

    # Element selection
    selected_element = st.selectbox("Select an element:", elements)

    # Display element information (from periodic table)
    if selected_element:
        element_data = periodic_table.get(selected_element)
        if element_data:
            st.subheader(f"{selected_element} - {element_data.get('name', '')}")
            st.write(f"Atomic Number: {element_data.get('atomic_number', '')}")
            st.write(f"Atomic Mass: {element_data.get('atomic_mass', '')}")
            st.write(f"Electron Configuration: {element_data.get('electron_configuration', '')}")

            # Placeholder for 3D atom visualization (using molecule_renderer)
            st.subheader("3D Atom Visualization (Placeholder)")
            # In a real implementation, you'd use the element data to construct
            # an atom model and pass it to render_3d_molecule
            # For example, you might load a predefined model or create one dynamically
            # using py3Dmol or a similar library.
            render_3d_molecule(element=selected_element, style='sphere')

        else:
            st.warning(f"No data found for {selected_element} in the periodic table.")
