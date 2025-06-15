import re
from fractions import Fraction
import math
def parse_equation(equation):
    # Remove spaces and split at '='
    lhs, rhs = equation.replace(" ", "").split('=')
    rhs = Fraction(rhs)

    # Find terms like +5x, -3y, z, -z
    pattern = re.compile(r'([+-]?[^+-]+)')
    terms = pattern.findall(lhs)

    coeffs = {'x': Fraction(0), 'y': Fraction(0), 'z': Fraction(0)}
    for term in terms:
        match = re.match(r'([+-]?[\d/]*)([xyz])', term)
        if match:
            num_str, var = match.groups()
            if num_str in ('', '+'):
                coeff = Fraction(1)
            elif num_str == '-':
                coeff = Fraction(-1)
            else:
                coeff = Fraction(num_str)
            coeffs[var] += coeff
    return [coeffs['x'], coeffs['y'], coeffs['z']], rhs


def ceil_round(val, decimals=3):
    factor = 10 ** decimals
    return math.ceil(val * factor) / factor


def jacobi(A, b, iterations=5):
    n = len(A)
    x = [Fraction(0)] * n
    for iteration in range(1, iterations + 1):
        x_new = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new

        print(f"Iteration {iteration}:")
        for idx, val in enumerate(x):
            decimal_val = float(val)
            rounded_val = ceil_round(decimal_val, 3)
            print(f"  x{idx + 1} = {val} ≈ {rounded_val:.3f}")
        print()
    return x


# --- MAIN PROGRAM ---
print("Enter 3 equations (example: 5x+4y-z=0)")
A = []
b = []

for i in range(3):
    eq = input(f"Equation {i + 1}: ")
    coeffs, rhs = parse_equation(eq)
    A.append(coeffs)
    b.append(rhs)

# Run Jacobi method
jacobi(A, b)

