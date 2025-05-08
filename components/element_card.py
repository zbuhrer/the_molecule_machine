import streamlit as st

def display_element_card(element_symbol, periodic_table_data):
    """
    Displays an element card with basic information.

    Args:
        element_symbol (str): The element symbol (e.g., "H", "O").
        periodic_table_data (dict): The periodic table data.
    """
    element_data = periodic_table_data.get(element_symbol)
    if element_data:
        with st.container():
            st.markdown(f"### {element_symbol} - {element_data.get('name', '')}")
            st.write(f"Atomic Number: {element_data.get('atomic_number', '')}")
            st.write(f"Atomic Mass: {element_data.get('atomic_mass', '')}")
            # You can add more details here as needed, e.g., electron configuration
    else:
        st.write(f"No data found for {element_symbol}")
