import numpy as np 

def f(x):
    return x[0]+x[1]+x[2]+x[3]

def fnumpy(x):
    return np.sum(x)

a = np.array([1,1,1,1])
b = np.array([1,0,1,0])
x,y = 1,-2

print('f(x*a + y*b) = ', f(x*a + y*b))