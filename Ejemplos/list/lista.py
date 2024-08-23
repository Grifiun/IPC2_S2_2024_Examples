# Una lista es un objeto mutable, se pueden cambiar los datos después de definidos

lista = [1, 2, "Hola a todos", ["Segunda lista elemento 1", "Mucho contenido"], "Ultimo valor"]
print(lista)

"""
Salida:
[1, 2, 'Hola a todos', ['Segunda lista elemento 1', 'Mucho contenido'], 'Ultimo valor']
"""

# Acceso a listas
# Inicia en la posición 0 en adelante, y -1 indica el último valor
print(lista[0])  # posición 0

print(lista[-1])  # Ultima posicion

print(lista[1:3])  # se puede usar X:Y para indicar de rango X hasta Y

"""
Salida:
1
Ultimo valor
[2, 'Hola a todos']
"""

# Adicional a eso, si seguimos haciendo más pequeño el numero negativo como -2
print(lista[-2])  # Penúltima posicion

"""
Salida: esta lista resultante es el penúltimo elemento de la lista principal
['Segunda lista elemento 1', 'Mucho contenido']
"""

# Asignar valores de una lista a variables
listaXYZ = ["x", "y", "z"]
x, y, z = listaXYZ
print("Estos son los valores de la listaXYZ: ", listaXYZ)
print("Valor de x : ", x)
print("Valor de y : ", y)
print("Valor de z : ", z)

"""
Salida:
Estos son los valores de la listaXYZ:  ['x', 'y', 'z']
Valor de x :  x
Valor de y :  y
Valor de z :  z
"""

# Crear una lista a partir de 2 listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# SALIDA: [1, 2, 3, 4, 5, 6]

# Contar las ocurrencias de un elemento en una lista
lista_concurrencia = [1, 1, 1, 3, 3, 2, 2, 2, 2]
print(lista_concurrencia.count(3))

# SALIDA: 2

# Mostrar el índice de la primera ocurrencia de un elemento
print(lista_concurrencia.index(2))

# SALIDA: 5
