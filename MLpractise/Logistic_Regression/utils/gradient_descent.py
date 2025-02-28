import copy
from .compute_gradient import compute_gradient
from .compute_cost import compute_cost
import math

def gradient_descent(X,y,w,b,alpha, iters = 10000):
    
    w_copy = copy.deepcopy(w)
    b_copy = b
    j_hist = []

    for i in range(iters):
        dj_dw, dj_db = compute_gradient(X,y,w_copy,b_copy)
        w_copy = w_copy - alpha * dj_dw
        b_copy = b_copy - alpha * dj_db

        if iters <= 10000:
            j_hist.append(compute_cost(X,y,w_copy,b_copy))

        if i % math.ceil(iters / 10) == 0:
            print(f"No. of iteration: {i} Cost: {j_hist[-1]}")

    return w_copy,b_copy, j_hist

if __name__ == "__main__":
    print("Use by importing it")
