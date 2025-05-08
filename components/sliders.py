
import streamlit as st

def temperature_slider(default_value=298.0, min_value=0.0, max_value=5000.0, step=1.0):
    """
    Creates a temperature slider.

    Args:
        default_value (float): The default temperature value in Kelvin.
        min_value (float): The minimum temperature value in Kelvin.
        max_value (float): The maximum temperature value in Kelvin.
        step (float): The step size for the slider.

    Returns:
        float: The selected temperature value in Kelvin.
    """
    temperature = st.slider(
        "Temperature (K)",
        min_value=min_value,
        max_value=max_value,
        value=default_value,
        step=step
    )
    return temperature


def pressure_slider(default_value=1.0, min_value=0.01, max_value=10.0, step=0.01):
    """
    Creates a pressure slider.

    Args:
        default_value (float): The default pressure value in atm.
        min_value (float): The minimum pressure value in atm.
        max_value (float): The maximum pressure value in atm.
        step (float): The step size for the slider.

    Returns:
        float: The selected pressure value in atm.
    """
    pressure = st.slider(
        "Pressure (atm)",
        min_value=min_value,
        max_value=max_value,
        value=default_value,
        step=step
    )
    return pressure
```
