import re
import numpy as np
from fractions import Fraction


def parse_equation(eq):
    eq = eq.replace(' ', '')
    left, right = eq.split('=')
    pattern = r'([+-]?\d*)([xyz])'
    matches = re.findall(pattern, left)

    coeffs = {'x': 0, 'y': 0, 'z': 0}

    for coeff, var in matches:
        if coeff in ('', '+'):
            coeff_val = 1
        elif coeff == '-':
            coeff_val = -1
        else:
            coeff_val = int(coeff)

        coeffs[var] += coeff_val

    const = int(right)

    return [coeffs['x'], coeffs['y'], coeffs['z']], const


def gauss_jordan(matrix, constants):
    n = len(constants)
    aug = np.hstack([matrix, constants.reshape(-1, 1)])

    for i in range(n):
        # Make the diagonal 1
        aug[i] = aug[i] / aug[i][i]
        for j in range(n):
            if i != j:
                aug[j] = aug[j] - aug[j][i] * aug[i]

    return aug[:, -1]


def to_fraction_array(arr):
    return [Fraction(val).limit_denominator() for val in arr]


def main():
    print("Enter 3 equations in form like 5x+6y-7z=11")
    matrix = []
    constants = []

    for i in range(3):
        eq = input(f"Equation {i + 1}: ")
        coeffs, const = parse_equation(eq)
        matrix.append(coeffs)
        constants.append(const)

    matrix = np.array(matrix, dtype=float)
    constants = np.array(constants, dtype=float)

    solution = gauss_jordan(matrix, constants)
    solution_frac = to_fraction_array(solution)

    print("\nSolution:")
    print(f"x = {solution_frac[0]}")
    print(f"y = {solution_frac[1]}")
    print(f"z = {solution_frac[2]}")


if __name__ == "__main__":
    main()
