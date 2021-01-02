rojo = [255,0,0]
verde = [0,255,0]
azul = [0,0,255]
# En python el operador + concatena listas y no suma los vectores, para solucionar este "problema" se utilizará la siguiente funcion

def suma_vectores(a,b):
    return [i+j for i,j in zip(a,b)]

print('la suma entre rojo y azul devuelve: ', suma_vectores(rojo, azul))

