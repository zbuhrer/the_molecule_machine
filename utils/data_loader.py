import json
import os
import streamlit as st
from config import PERIODIC_TABLE_JSON, LESSONS_MD

def load_periodic_table() -> dict:
    """
    Loads the periodic table data from the JSON file.

    Returns:
        dict: A dictionary containing the periodic table data,
              or an empty dictionary if the file is not found or there's an error.
    """
    try:
        with open(PERIODIC_TABLE_JSON, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"Error: Periodic table data file not found at {PERIODIC_TABLE_JSON}")
        return {}
    except json.JSONDecodeError:
        st.error(f"Error: Could not decode JSON from {PERIODIC_TABLE_JSON}")
        return {}
    except Exception as e:
        st.error(f"An unexpected error occurred while loading periodic table data: {e}")
        return {}

def load_orbitals():
    """
    Placeholder for loading orbital data.  Not yet implemented.
    """
    # In a real implementation, you would load orbital data, perhaps from a 3D model file.
    pass


def load_lessons_markdown() -> dict:
    """
    Loads lessons from a Markdown file.

    Returns:
        dict: A dictionary with lesson titles as keys and lesson content (markdown) as values,
              or an empty dictionary if the file is not found or there's an error.
    """
    lessons = {}
    try:
        with open(LESSONS_MD, "r") as f:
            lines = f.readlines()

        title = None
        content = ""
        for line in lines:
            if line.startswith("# "):  # Assuming lessons start with a level 1 heading
                if title:
                    lessons[title] = content.strip()
                title = line[2:].strip()  # Extract title, removing "# "
                content = ""
            elif title:
                content += line
        if title:
            lessons[title] = content.strip()

    except FileNotFoundError:
        st.error(f"Lessons file not found: {LESSONS_MD}")
        return {}
    except Exception as e:
        st.error(f"An error occurred while loading lessons: {e}")
        return {}

    return lessons
