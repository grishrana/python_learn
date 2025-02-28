import numpy as np 
from .sigmoid import sigmoid

def predict(X,w,b):
    m = X.shape[0]
    y_pred = np.array([])
    for i in range(m):
        z_in = np.dot(w,X[i]) + b
        y_pred_i = sigmoid(z_in)
        y_pred = np.append(y_pred,y_pred_i)

    return y_pred
