import streamlit as st
import py3Dmol
from logging_config import logger
from utils.data_loader import load_periodic_table

def render_3d_molecule(element=None, xyz_coordinates=None, style="stick"):
    """
    Renders a 3D molecule using py3Dmol.

    Args:
        element (str, optional): The element symbol (e.g., "H", "O\").
        xyz_coordinates (list of tuples, optional): A list of (x, y, z) coordinates.
        style (str, optional): The style of the molecule rendering ("stick", "sphere", etc.). Defaults to "stick".
    """
    logger.info(f"render_3d_molecule called with element={element}, xyz_coordinates={xyz_coordinates}, style={style}")
    if element is None and xyz_coordinates is None:
        st.warning("No molecule data provided.")
        logger.warning("No molecule data provided to render_3d_molecule.")
        return

    view = py3Dmol.view()

    if element:
        periodic_table = load_periodic_table()
        element_data = periodic_table.get(element)

        if not element_data:
            st.warning(f"No data found for {element} in the periodic table.")
            logger.warning(f"No data found for element {element} in periodic table.")
            return

        vdw_radius = element_data.get("vdw_radius", 1.5)
        color = element_data.get("color", "red")
        crystal_structure = element_data.get("crystal_structure", None)
        lattice_parameter = element_data.get("lattice_parameter", None)
        atomic_positions = element_data.get("atomic_positions", [])

        logger.debug(f"Rendering element {element} with vdw_radius={vdw_radius}, color={color}, crystal_structure={crystal_structure}, lattice_parameter={lattice_parameter}, atomic_positions={atomic_positions}")

        if crystal_structure and lattice_parameter and atomic_positions:
            # Render crystal structure
            for position in atomic_positions:
                x = position[0] * lattice_parameter
                y = position[1] * lattice_parameter
                z = position[2] * lattice_parameter
                view.addSphere({"center": [x, y, z], "radius": vdw_radius, "color": color})
        else:
            # Render single atom
            view.addSphere({"center": [0, 0, 0], "radius": vdw_radius, "color": color})

        view.zoomTo()
        #view.setStyle({"sphere": {"radius": 0.5}})  #Styling was not working
    elif xyz_coordinates:
        for i, coords in enumerate(xyz_coordinates):
            view.addSphere({"center": coords, "radius": 0.5, "color": "lightgray"})  # Basic sphere for now
        view.zoomTo()
        view.setStyle({style: {}})  # Apply the specified style
    st.markdown(view.js(), unsafe_allow_html=True)
    logger.info("render_3d_molecule finished.")

def display_orbitals(element):
    """
    Placeholder for displaying atomic orbitals.  This will need to be expanded
    to load orbital data and render it.
    """
    st.write(f"Displaying orbitals for {element} (Placeholder - not implemented yet)")
    logger.warning(f"display_orbitals called for {element}, but is a placeholder.")
    # In a real implementation, you would:
    # 1. Load orbital data (e.g., from a file or calculation).
    # 2. Use py3Dmol or a similar library to render the 3D orbitals.
