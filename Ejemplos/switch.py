def opciones(numero):
        match numero:
            case 1:
                print("Opción 1: Seleccionaste el número uno.")
            case 2:
                print("Opción 2: Seleccionaste el número dos.")
            case 3:
                print("Opción 3: Seleccionaste el número tres.")
            case 4:
                print("Opción 4: Seleccionaste el número cuatro.")
            case 5:
                print("Opción 5: Seleccionaste el número cinco.")
            case _:
                print("Opción no válida: Seleccionaste un número fuera del rango 1-5.")

if __name__ == "__main__":
    #main()   
    # Ejemplo de uso
    opciones(3)
    opciones(2)
