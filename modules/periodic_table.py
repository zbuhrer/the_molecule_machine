import streamlit as st
import pandas as pd
from utils.data_loader import load_periodic_table
from components.element_card import display_element_card

def render():
    st.header("Interactive Periodic Table")

    try:
        periodic_table_data = load_periodic_table()
        df = pd.DataFrame.from_dict(periodic_table_data, orient='index')
        df.index.name = 'Symbol'  # Set the index name to 'Symbol'
    except FileNotFoundError:
        st.error("Error: Could not load periodic table data. Make sure periodic_table.json exists in the data directory.")
        return

    # Sidebar filter options
    with st.sidebar:
        st.subheader("Filter Elements")
        element_types = sorted(df['group'].unique().tolist())
        selected_type = st.selectbox("Select Group:", ['All'] + element_types)

    # Apply filter
    if selected_type != 'All':
        df_filtered = df[df['group'] == selected_type]
    else:
        df_filtered = df

    # Display the table using columns for better layout
    num_cols = 7  # Adjust as needed for the layout
    elements = df_filtered.index.tolist()
    for i in range(0, len(elements), num_cols):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            index = i + j
            if index < len(elements):
                element_symbol = elements[index]
                with cols[j]:
                    display_element_card(element_symbol, periodic_table_data)
