import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """

    # Write code here
    i = 0
    w = np.zeros(X.shape[1])
    b = 0.0
    
    while i < steps:

        p = _sigmoid(np.add(np.matmul(X, w), b))
        grad_w = np.matmul(np.transpose(X), np.subtract(p,y))/len(y)
        grad_b = np.mean(np.subtract(p,y))

        w = np.subtract(w,lr*grad_w)
        b = np.subtract(b,lr*grad_b)

        i+=1

    return w,b
    pass