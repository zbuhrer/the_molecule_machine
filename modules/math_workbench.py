import streamlit as st
import sympy
import matplotlib.pyplot as plt
import numpy as np

from utils.equations import solve, latexify

def render():
    st.header("Math Workbench")

    # Equation Solver
    st.subheader("Equation Solver")
    equation_input = st.text_input("Enter an equation (e.g., x + 2 = 5):", "x + 2 = 5")
    if st.button("Solve"):
        try:
            solution = solve(equation_input)
            if solution:
                st.success(f"Solution: {latexify(solution)}")
                st.latex(latexify(solution))
            else:
                st.warning("No solution found.")
        except Exception as e:
            st.error(f"Error solving equation: {e}")

    # Plotting
    st.subheader("Function Plotter")
    function_input = st.text_input("Enter a function of x (e.g., x**2 + 2*x + 1):", "x**2")
    x_min = st.number_input("x min:", value=-5.0)
    x_max = st.number_input("x max:", value=5.0)
    num_points = st.number_input("Number of points:", value=100)

    if st.button("Plot"):
        try:
            x = np.linspace(x_min, x_max, int(num_points))
            # Use sympy to parse and evaluate the function
            x_sym = sympy.symbols('x')
            function_sym = sympy.sympify(function_input, locals={'x': x_sym})
            y = [function_sym.subs(x_sym, val) for val in x]

            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.set_title("Function Plot")
            ax.grid(True)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting function: {e}")
