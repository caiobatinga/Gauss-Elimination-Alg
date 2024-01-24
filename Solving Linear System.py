import numpy as np

def forward_substitution(L, b):
    n = len(b)
    x = [0] * n

    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= L[i][j] * x[j]
        x[i] /= L[i][i]

    return x

def backward_substitution(U, b):
    n = len(b)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

def transform_upper_lower(U):
    n = len(U)
    L = np.eye(n)


    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            factor = U[j][i] / U[i][i]
            U[j] -= factor * U[i]
            L[j][i] = factor

    return L



def gauss_elimination(A, b):
    n = len(b)

    print("Initial Values:")
    print("A:")
    print_matrix(A)
    print("b:", b)

    # Forward Elimination
    for i in range(n):
        pivot = A[i][i]
        print(f"\nStep {i + 1}:")
        print(f"Pivot: {pivot}")

        for k in range(i + 1, n):
            factor = A[k][i] / pivot
            print(f"\nRow {k + 1} -= {factor:.2f} * Row {i + 1}")

            for j in range(i, n):
                A[k][j] -= factor * A[i][j]

            b[k] -= factor * b[i]

        print_matrix(A)
        print("b:", b)

    return A, b

def print_matrix(matrix):
    for row in matrix:
        print(row)


if __name__ == '__main__':

    A = [
        [1, 2, 1, -1],
        [3, 2, 4, 4],
        [4, 4, 3, 4],
        [2, 0, 1, 5]
    ]

    b = [5, 16, 22, 15]


    A_transformed, b_transformed = gauss_elimination(A, b)


    print("\nFinal System:")
    print("A:")
    print_matrix((A_transformed))
    print("b:", b_transformed)

    x = backward_substitution(A, b)
    print("X values: ",x)


