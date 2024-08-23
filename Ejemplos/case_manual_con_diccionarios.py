# Definir los bloques de funciones
def opcion_1():
    print("Opción 1: Seleccionaste el número uno.\n")

def opcion_2():
    print("Opción 2: Seleccionaste el número dos.\n")

def opcion_3():
    print("Opción 3: Seleccionaste el número tres.\n")

def opcion_4():
    print("Opción 4: Seleccionaste el número cuatro.\n")

def opcion_5():
    print("Opción 5: Seleccionaste el número cinco.\n")

# Mapear las entradas a los bloques de funciones
opciones = {
    1: opcion_1,
    2: opcion_2,
    3: opcion_3,
    4: opcion_4,
    5: opcion_5
}

# Invocar el bloque equivalente al switch
def ejecutar_opcion(num):
    # Ejecuta la función correspondiente al número, si existe
    if num in opciones:
        opciones[num]()
    else:
        print("Opción no válida: Seleccionaste un número fuera del rango 1-5.\n")

if __name__ == "__main__":
    # Ejemplo de uso
    ejecutar_opcion(3)