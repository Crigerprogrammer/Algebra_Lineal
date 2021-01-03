import numpy as np 

a = np.array([1,0,0,0])
b = np.array([0,0,1,0])

# Para hacer producto punto en python con nympy se utiliza la función .dot
print('Producto punto de a y b es ', np.dot(a,b))

# Para transponer en python se utiliza T y luego @ para indicar que vector
print('Producto punto con transpuesta de a y b es ', a.T@b)