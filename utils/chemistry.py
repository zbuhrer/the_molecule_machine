import re
from typing import Dict, Union
from sympy import Symbol, sympify, Float, Integer, parse_expr

def parse_formula(formula: str) -> Dict[str, int]:
    """
    Parses a chemical formula and returns a dictionary of element symbols and their counts.

    Args:
        formula (str): The chemical formula (e.g., "H2O", "C6H12O6").

    Returns:
        Dict[str, int]: A dictionary where keys are element symbols and values are their counts.
                          Returns an empty dictionary if the formula is invalid.
    """
    element_counts: Dict[str, int] = {}
    matches = re.findall(r"([A-Z][a-z]*)(\d*)", formula)  # Match element symbols and their counts

    for match in matches:
        element = match[0]
        count_str = match[1]
        count = int(count_str) if count_str else 1  # Default count to 1 if not specified
        element_counts[element] = element_counts.get(element, 0) + count

    return element_counts


def calculate_mass(formula: str) -> float:
    """
    Calculates the molar mass of a chemical formula using approximate atomic masses.

    Args:
        formula (str): The chemical formula (e.g., "H2O", "CH4").

    Returns:
        float: The molar mass in g/mol.  Returns 0 if the formula is invalid or has an issue.
    """
    element_masses = {
        "H": 1.008, "C": 12.011, "O": 16.00, "N": 14.007, "Cl": 35.45,
        "Na": 22.99, "Mg": 24.305, "S": 32.06, "P": 30.974, "K": 39.10,
        "Ca": 40.078, "Fe": 55.845
    }
    try:
        parsed_formula = parse_formula(formula)
        total_mass = 0.0
        for element, count in parsed_formula.items():
            if element in element_masses:
                total_mass += element_masses[element] * count
            else:
                raise ValueError(f"Element '{element}' not found in element_masses.")
        return total_mass
    except (ValueError, TypeError) as e:
        print(f"Error calculating mass for {formula}: {e}")  #debugging
        return 0.0


def reaction_energy():
    """
    Placeholder for calculating reaction energy.  Needs further implementation.
    """
    pass
