import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def plot_function(x_min: float, x_max: float, num_points: int, function_str: str):
    """
    Plots a mathematical function using Matplotlib and displays it in Streamlit.

    Args:
        x_min (float): The minimum x-value for the plot.
        x_max (float): The maximum x-value for the plot.
        num_points (int): The number of points to use for the plot.
        function_str (str): The mathematical function as a string,
                            e.g., "x**2 + 2*x + 1".  Uses numpy for calculations.
    """
    try:
        x = np.linspace(x_min, x_max, num_points)
        y = eval(function_str, {'x': x, 'np': np})  # Evaluate the function
        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Function Plot")
        ax.grid(True)
        st.pyplot(fig)

    except (ValueError, TypeError, SyntaxError, NameError) as e:
        st.error(f"Error plotting function: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
