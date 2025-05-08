import streamlit as st
from utils.chemistry import parse_formula, calculate_mass
import sympy
from sympy.parsing.mathematica import parse_mathematica
from sympy import Eq, solve

def render():
    st.header("Reaction Simulator")

    # Input fields for reactants and products
    st.subheader("Enter Reactants and Products")
    reactants_input = st.text_input("Reactants (e.g., CH4 + O2)", "CH4 + O2")
    products_input = st.text_input("Products (e.g., CO2 + H2O)", "CO2 + H2O")

    # Button to balance the equation
    if st.button("Balance Equation"):
        try:
            balanced_equation_str, reaction_equation, balanced_coeffs = balance_equation(reactants_input, products_input)
            if balanced_equation_str:
                st.success(f"Balanced Equation: {balanced_equation_str}")

                # Calculate and display molar masses
                st.subheader("Molar Masses")
                for compound, coeff in zip(reaction_equation.split("=")[0].split("+") + reaction_equation.split("=")[1].split("+"), balanced_coeffs):
                    compound = compound.strip()
                    if compound:
                        try:
                            mass = calculate_mass(compound)
                            st.write(f"{compound}: {mass:.2f} g/mol")
                        except Exception as e:
                            st.warning(f"Could not calculate molar mass for {compound}: {e}")

        except Exception as e:
            st.error(f"Error balancing equation: {e}")

    # Simulation controls (placeholder - will be expanded)
    st.subheader("Simulation Controls (Placeholder)")
    st.write("Temperature, Pressure, etc. controls will be added here later.")


def balance_equation(reactants_input, products_input):
    try:
        reactants = [s.strip() for s in reactants_input.split("+")]
        products = [s.strip() for s in products_input.split("+")]

        # Parse formulas and create symbolic variables
        elements = set()
        for compound in reactants + products:
            if compound:
                for element in parse_formula(compound).keys():
                    elements.add(element)

        element_list = sorted(list(elements))
        num_elements = len(element_list)

        # Create symbolic variables for coefficients
        coeffs = sympy.symbols("c1:" + str(len(reactants) + len(products) + 1))
        coeff_dict = {}
        i = 0
        for compound in reactants + products:
            coeff_dict[compound] = coeffs[i]
            i += 1


        # Create equations for each element
        equations = []
        reactant_side = ""
        product_side = ""
        eq_str = ""
        balanced_coeffs = []

        for element in element_list:
            equation = 0
            eq_str = ""
            for i, compound in enumerate(reactants + products):
                if compound:
                    parsed_formula = parse_formula(compound)
                    if element in parsed_formula:
                        coeff = coeff_dict[compound]
                        count = parsed_formula[element]
                        equation += coeff * count
                        if i < len(reactants):
                            reactant_side += f" + {coeff}*{count} ({compound})"
                        else:
                            product_side += f" + {coeff}*{count} ({compound})"

            equations.append(equation)

        # Solve the equations
        solutions = sympy.solve(equations, coeffs)

        # Find the solution with the smallest integer values
        if solutions:
            # Substitute solution into the equations and get coefficients
            for i in range(len(coeffs)):
                if coeffs[i] in solutions:
                    val = solutions[coeffs[i]]
                    balanced_coeffs.append(val)
                else:
                    balanced_coeffs.append(0)

            # Convert to integers and normalize

            balanced_coeffs = [float(x) for x in balanced_coeffs]
            gcd_val = 1.0

            for val in balanced_coeffs:
              if val != 0:
                  gcd_val = gcd_val * val / sympy.gcd(gcd_val,val)

            balanced_coeffs = [round(x/gcd_val) for x in balanced_coeffs]


            # Construct the balanced equation string
            balanced_equation_str = ""
            reactant_str = ""
            product_str = ""
            i = 0
            for compound in reactants:
                if compound:
                    reactant_str += f" + {balanced_coeffs[i]} {compound}"
                    i+=1

            for compound in products:
                if compound:
                    product_str += f" + {balanced_coeffs[i]} {compound}"
                    i+=1

            reactant_str = reactant_str.replace(" + ", "", 1)
            product_str = product_str.replace(" + ", "", 1)
            balanced_equation_str = f"{reactant_str} = {product_str}"

            return balanced_equation_str, f"{reactants_input} = {products_input}", balanced_coeffs
        else:
            return None, None, None
    except Exception as e:
        raise Exception(f"Error during balancing: {e}")
