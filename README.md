## Algebra Lineal : Vectores
---

### Vectores:
Un vector es una lista finita de números. Los podemos encontrar en dos presentaciones:
- Vector Columna
- Vector renglón

Hay dos estructuras: **espacios vectoriales y campos**. De manera simplificada los *números* viven en los campos mientras que los vectores viven en los espacios *vectoriales*.

Existen **Bloque o stack de vectores**. Es un vector que tiene dentro más vectores.

**Subvectores** Son una porción de un vector y se detona con : para limitar el indice de inicio y el final

**Cero Vectores**: Un cero vector es un vector donde todos los elementos son 0. Ejemplo: **0** = (0,0)

**Uno Vectores** Un uno vector es un vector donde todos los elementos son 1. Ejemplo: **1** = (1,1)

**Vectores Unitarios** Un vector unitario es aquel donde todos sus elementos son 0, menos un elemento con valor 1. Ejemplo: **a** = (0,1,0)

### Vectores en Python
Los vectores en python se representan con la estructura de datos *listas*, como ejemplo: rojo=[255,0,0] 

### Adición entre vectores
Los vectores de la misma dimensión se pueden sumar elemento a elemento, esta operación es denotada por el operador **+**.
*OJO*: Únicamente se pueden sumar vectores de la misma dimensión
Ejemplo:
 (1,2,3) + (-1,-2,-3) = (1 -1, 2 - 2, 3 - 3) = (0, 0, 0) = 0

### Propiedades de la adición entre vectores
La adición entre vectores cumple ciertas propiedades, las cuales son:
- La suma de vectores es conmutativa:
    - a + b = b + a
- La suma de vectores es asociativa:
    - (a+b) + c = a + (b+c)
- La suma entre vectores, cuando hay un vector 0, no surte algún efecto:
    - a + 0 = 0 + a = a
- Sumar un vector con su inverso (vector negativo), da como resultado 0
    - a + (-a) = 0 

## Numpy
Numpy es una biblioteca de Python que nos proporciona funciones para operar vectores, matrices y entre otras operaciones de alto nivel matemáticas

### Producto escalar-vector
Para la multiplicación de un escalar y vector, el escalar se multiplica por cada elemento interno del vector. Ejemplo:
- vector v(0,1,-2.3) * escalar a=-1.1 = av -1.1*(0,1,-2.3) es decir:
- av = (-1.1x0, -1.1x1, -1.1x-2.3) = (0, -1,1, 2.53)

### Propiedades del producto escalar-vector
Al igual que la suma la multiplicacion entre escalar y vector tiene una cantidad de propiedades, las cuales son:
- Conmutativa: ax = xa
- Asociativa (ab)x = a(bx)
- Distribución sobre suma escalar: (a + b)x = ax + bx 
- Distribución sobre suma de vectores: a(x + y) = ax + ay

### Producto por escalar en Python
Para realizar la operación producto entre un vector y escalar en python, bastará con importar la librería numpy, declarar un arreglonumpy y posteriormente multiplicar por cualquier escalar y se realizará la multiplicación del escalar por cada elemento del vector.

- Ejercicio:
considerando $\vec{v} = (1,1)$. Si consideramos a = -1, b = 2, c = 0.1

### Producto Interno
O también conocido como producto punto, es el producto de dos vectores.
Simplemente es la suma del producto de sus entradas.