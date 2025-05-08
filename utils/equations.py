import sympy
from sympy import Eq, solve, latex
from sympy.parsing.mathematica import parse_mathematica

def solve(equation_str: str):
    """
    Solves an equation and returns the solution.

    Args:
        equation_str (str): The equation to solve (e.g., "x + 2 = 5").

    Returns:
        sympy.core.expr.Expr: The solution of the equation.
    """
    try:
        # Replace Mathematica-style "==" with "="
        equation_str = equation_str.replace("==", "=")

        # Parse the equation
        lhs, rhs = equation_str.split("=")
        x = sympy.symbols("x")
        lhs_expr = parse_mathematica(lhs)
        rhs_expr = parse_mathematica(rhs)
        equation = Eq(lhs_expr, rhs_expr)

        # Solve the equation
        solution = sympy.solve(equation, x)
        return solution
    except Exception as e:
        print(f"Error solving equation: {e}") #debugging
        return None

def latexify(expression):
    """
    Converts a SymPy expression to a LaTeX formatted string.

    Args:
        expression: The SymPy expression.

    Returns:
        str: The LaTeX representation of the expression.
    """
    try:
        return latex(expression)
    except Exception as e:
        print(f"Error converting to LaTeX: {e}") #debugging
        return str(expression)
