import numpy as np 
def gradF(z):
    return np.array([1-np.exp(z[1]-z[0]), np.exp(z[1]-z[0])])

z = np.array([1, 2])
print('grad(f)[1,2 = ', gradF(z))

def taylor_F(x,z):
    fz = F(z)
    gz = gradF(z)
    return fz + gz@(x-z)

print('Taylor es: ,', taylor_F(z,z))

def df(z):
    return 2*z - 3*z**2

def tf(x,z):
    return f(z) + df(z)*(x-z)
