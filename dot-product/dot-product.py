import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    if len(x) == len(y):
        total = 0
        for i in range(len(x)):
            total += x[i]*y[i]

    else:
        print("Vector dimensions must be same!")

    total = float(total)
    pass
    return total