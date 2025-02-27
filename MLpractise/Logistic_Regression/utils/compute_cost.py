import numpy as np 
from .sigmoid import sigmoid

def compute_cost(x,y,w,b):
    cost = 0
    m = x.shape[0]
    for i in range(m):
        z_i = np.dot(w,x[i]) + b
        f_wb = sigmoid(z_i)
        loss = y[i]*np.log(f_wb) + (1-y[i])*np.log(1-f_wb)
        cost = cost + loss

    cost = -(cost/m)

    return cost

if __name__ == "__main__":
    print("Import")
