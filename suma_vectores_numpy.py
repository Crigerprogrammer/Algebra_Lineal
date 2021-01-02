import numpy as np

rojo = [255,0,0]
verde = [0,255,0]
azul = [0,0,255]

# Numpy tiene una estructura de datos llamado numpy arrays y se pueden crear con la propiedad array
# Los numpy array tienen las propiedades de un vector y su suma puede ser como los vectores algebraicos
rojo = np.array(rojo)
verde = np.array(verde)
azul = np.array(azul)

print('La suma de los numpy array rojo mas verde es: ', rojo+verde)
