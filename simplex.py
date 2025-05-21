import numpy as np

def simplex_full_solver(c, A, b):
    """
    Solves the Linear Programming problem:
    Maximize:     c^T x
    Subject to:   A x <= b, x >= 0

    Uses the Simplex algorithm (tableau method).
    """
    num_vars = len(c)
    num_constraints = len(b)

    # Create the initial tableau with slack variables
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))

    # Fill constraint coefficients and slack variables
    for i in range(num_constraints):
        tableau[i, :num_vars] = A[i]
        tableau[i, num_vars + i] = 1  # Slack variable
        tableau[i, -1] = b[i]

    # Fill the last row with the negated objective function coefficients
    tableau[-1, :num_vars] = -np.array(c)

    # Start the Simplex loop
    while True:
        # Step 1: Find entering variable (most negative coefficient in bottom row)
        pivot_col = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col] >= 0:
            break  # Optimal solution found

        # Step 2: Find leaving variable (smallest positive ratio of RHS to pivot col)
        ratios = []
        for i in range(num_constraints):
            if tableau[i, pivot_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(np.inf)

        pivot_row = np.argmin(ratios)
        if ratios[pivot_row] == np.inf:
            raise ValueError("Problem is unbounded.")

        # Step 3: Pivot operation
        pivot_val = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_val  # Make pivot = 1
        for i in range(num_constraints + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    # Extract the solution
    solution = np.zeros(num_vars)
    for i in range(num_vars):
        col = tableau[:, i]
        if np.count_nonzero(col[:-1]) == 1 and np.isclose(np.sum(col[:-1]), 1):
            row = np.argmax(col[:-1])
            solution[i] = tableau[row, -1]

    optimal_value = tableau[-1, -1]
    return solution, optimal_value


# Example Problem:
# Maximize Z = 3x + 2y
# Subject to:
# 2x + y <= 18
# 2x + 3y <= 42
# 3x + y <= 24

c = [3, 2]
A = [
    [2, 1],
    [2, 3],
    [3, 1]
]
b = [18, 42, 24]

solution, optimal_value = simplex_full_solver(c, A, b)

print("Optimal solution:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val}")
print(f"Maximum value of Z = {optimal_value}")