import numpy as np

rojo = [255,0,0]
verde = [0,255,0]
azul = [0,0,255]
negro = [0,0,0]

# Numpy tiene una estructura de datos llamado numpy arrays y se pueden crear con la propiedad array
# Los numpy array tienen las propiedades de un vector y su suma puede ser como los vectores algebraicos
rojo = np.array(rojo)
verde = np.array(verde)
azul = np.array(azul)

print('La suma de los numpy array rojo mas verde es: ', rojo+verde)

# Ejercicio de clase #6
# vector a = [0,0,255] es el color azul

# Color al sumar rojo verde y azul
print('La suma de los vectores, rojo, verde y azul es: ', rojo+verde+azul)
# Color sumando rojo y verde
print('La suma de los vectores, rojo y verde es: ', rojo+verde)
# Color sumando negro - azul es:
print('La suma negro menos azul es: ', negro-(+azul))