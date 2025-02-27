import numpy as np

def sigmoid(z):
    res = 1 / (1+np.exp(-z))
    return res

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    res = sigmoid(n)
    print(f"Sigmoid : {res}\n")
    

