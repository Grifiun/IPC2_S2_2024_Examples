# Una tupla es un objeto inmutable, no pueden cambiar los datos una vez definidos


tupla = (1, 2, "Hola a todos", ("Segunda tupla elemento 1", "Mucho contenido"), "Ultimo valor")
print (tupla)

"""
Salida:
(1, 2, 'Hola a todos', ('Segunda tupla elemento 1', 'Mucho contenido'))
"""

# Acceso a tuplas
# Inicia en la posición 0 en adelante, y -1 indica el último valor
print(tupla[0]) # posición 0

print(tupla[-1]) # Ultima posicion

print(tupla[1:3]) # se puede usar X:Y para indicar de rango X hasta Y

"""
Salida:
1
Ultimo valor
(2, 'Hola a todos')
"""

# Adicional a eso, si seguimos haciendo más pequeño el numero negativo como -2
print(tupla[-2]) # Penúltima posicion

"""
Salida: esta tupla resultante es el penúltimo elemento de la tupla principal
('Segunda tupla elemento 1', 'Mucho contenido')
"""

# Asignar valores de una tupla a variables
tuplaXYZ = ("x", "y", "z")
x, y, z = tuplaXYZ
print("Estos son los valores de la tuplaXYZ: ", tuplaXYZ)
print("Valor de x : ", x)
print("Valor de y : ", y)
print("Valor de z : ", z)

"""
Salida: 
Estos son los valores de la tuplaXYZ:  ('x', 'y', 'z')
Valor de x :  x
Valor de y :  y
Valor de z :  z
"""

# Crear una tupla a partir de 2 tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)

# SALIDA: (1, 2, 3, 4, 5, 6)

# Contar las ocurrencias de un elemento en una tupla
tupla_concurrencia = (1, 1, 1, 3, 3, 2, 2, 2, 2)
print(tupla_concurrencia.count(3))

# SALIDA: 2

# Mostrar el índice de la primera ocurrencia de un elemento
print(tupla_concurrencia.index(2))

# SALIDA: 5