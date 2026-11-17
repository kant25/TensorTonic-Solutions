import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dot_product = np.dot(a,b)
    A = np.sqrt(np.sum(np.square(a)))
    B = np.sqrt(np.sum(np.square(b)))
    if A != 0 and B != 0:
        cos = float(dot_product/(A*B))
    else:
        cos = 0.0
    pass
    return cos