import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    a = np.array(matrix, dtype=float)

    if axis == 0 and norm_type == 'l1':
        for i in range(a.shape[1]):
            column = a[:, i]
            col_norm = np.sum(np.abs(column))
            if col_norm != 0:
                for j in range(column.size):
                    a[j][i] = a[j][i] / col_norm
        return a

    elif axis == 0 and norm_type == 'l2':
        for i in range(a.shape[1]):
            column = a[:, i]
            col_norm = np.sqrt(np.sum(np.square(column)))
            if col_norm != 0:
                for j in range(column.size):
                    a[j][i] = a[j][i] / col_norm
        return a

    elif axis == 0 and norm_type == 'max':
        for i in range(a.shape[1]):
            column = a[:, i]
            col_norm = np.max(np.abs(column))
            if col_norm != 0:
                for j in range(column.size):
                    a[j][i] = a[j][i] / col_norm
        return a

    elif axis == 1 and norm_type == 'l1':
        for i in range(a.shape[0]):
            row = a[i, :]
            row_norm = np.sum(np.abs(row))
            if row_norm != 0:
                for j in range(row.size):
                    a[i][j] = a[i][j] / row_norm
        return a

    elif axis == 1 and norm_type == 'l2':
        for i in range(a.shape[0]):
            row = a[i, :]
            row_norm = np.sqrt(np.sum(np.square(row)))
            if row_norm != 0:
                for j in range(row.size):
                    a[i][j] = a[i][j] / row_norm
        return a

    elif axis == 1 and norm_type == 'max':
        for i in range(a.shape[0]):
            row = a[i, :]
            row_norm = np.max(np.abs(row))
            if row_norm != 0:
                for j in range(row.size):
                    a[i][j] = a[i][j] / row_norm
        return a

    elif axis is None and norm_type == 'l1':
        mat_norm = np.sum(np.abs(a))
        if mat_norm != 0:
            for i in range(a.shape[0]):
                for j in range(a.shape[1]):
                    a[i][j] = a[i][j] / mat_norm
        return a

    elif axis is None and norm_type == 'l2':
        mat_norm = np.sqrt(np.sum(np.square(a)))
        if mat_norm != 0:
            for i in range(a.shape[0]):
                for j in range(a.shape[1]):
                    a[i][j] = a[i][j] / mat_norm
        return a

    elif axis is None and norm_type == 'max':
        mat_norm = np.max(np.abs(a))
        if mat_norm != 0:
            for i in range(a.shape[0]):
                for j in range(a.shape[1]):
                    a[i][j] = a[i][j] / mat_norm
        return a