import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    n = len(A)
    m = len(A[0])

    B = [[0]*n for _ in range(m)]
    

    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]

    B = np.array(B)

    return B
    pass
