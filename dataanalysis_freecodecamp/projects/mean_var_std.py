import numpy as np


def calculate(data):

    mean=[]
    variance=[]
    standard_deviation=[]
    max=[]
    min=[]
    sum=[]

    if(len(data)<9):
        raise ValueError("List must contain nine numbers.")

    np_array=np.array(data).reshape(3,3)
    solution={
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    
    #calculating the values axis=1 means row and axis=0 means column

    for i in range(2):
            mean.append(list(np_array.mean(axis=i)))
            variance.append(list(np_array.var(axis=i)))
            standard_deviation.append(list(np_array.std(axis=i)))
            max.append(list(np_array.max(axis=i)))
            min.append(list(np_array.min(axis=i)))
            sum.append(list(np_array.sum(axis=i)))

    
    mean.append(np_array.mean())
    variance.append(np_array.var())
    standard_deviation.append(np_array.std())
    max.append(np_array.max())
    min.append(np_array.min())
    sum.append(np_array.sum())


    solution['mean']=mean
    solution['variance']=variance
    solution['standard deviation']=standard_deviation
    solution['max']=max
    solution['min']=min
    solution['sum']=sum

    return solution


data=[0,1,2,3,4,5,6,7,8]
sol=calculate(data)

print(sol)
