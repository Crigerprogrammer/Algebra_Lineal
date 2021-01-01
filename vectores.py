rojo = [255,0,0]
verde = [0,255,0]
azul = [0,0,255]
# Los vectores en Python se representan con la estructura de datos lista
tupla = (1,1,1)
# Las tuplas son otra estructura de datos pero son imutables 
print(type(rojo))
print(type(tupla))

print('El color rojo se representa con el vector ', rojo)
print('El color verde se representa con el vector', verde)
print('El color azul se representa con el vector', azul)

# Para conocer la dimensión de un vector, podemos utilizar el método len
print('La dimensión del vector rojo es ', len(rojo))

# Se pueden sumar vectores y así mismo crear stacks de vectores
rojo_verde = rojo + verde 
print('La suma del vector rojo y verde es ', rojo_verde)

# Se puede hacer sub vectores en python indicando del subindice que parte el vector hasta el ultimo subindice
print('Se partira el vector rojo ', rojo[0:2])

