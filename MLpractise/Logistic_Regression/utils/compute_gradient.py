import numpy as np
from .sigmoid import sigmoid

def compute_gradient(X,y,w,b):
    m,n = X.shape
    
    dj_dw = np.zeros((n,))
    dj_db = 0
    for i in range(m):
        z_i = np.dot(w,X[i]) + b 
        f_wb_i = sigmoid(z_i)
        err_i = y[i] - f_wb_i
        
        for j in range(n):
            dj_dw[j] = dj_dw[j] + (err_i * X[i,j])

        dj_db += err_i

    dj_db = -(dj_db/m)
    dj_dw = -(dj_dw/m)

    return (dj_dw,dj_db)

if __name__ == "__main__":
    print("Use by importing it")
