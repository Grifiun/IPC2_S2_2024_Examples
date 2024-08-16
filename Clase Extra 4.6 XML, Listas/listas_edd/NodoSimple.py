class NodoSimple:
    def __init__(self, texto):
        print(f"Se creo nodo, {texto}")
        self.texto = texto
        self.siguiente = None
        
    def agregarSiguiente(self, nodo):
        self.siguiente = nodo
        print(f"{self.texto} -> siguiente -> {nodo.texto}")

    def imprimirTexto(self):
        if(self.siguiente != None):
            print(f"{self.texto} -> {self.siguiente.texto}")
        else:
            print(f"{self.texto}")

    #def __next__(self)
    #    return self.texto

if __name__ == "__main__":
    print("Ejecutando Main de Nodo")

    # Crear nodos
    nodo1 = NodoSimple("Nodo1")

    # Al crear nodo2, actualizamos el siguiente de Nodo1
    nodo2 = NodoSimple("Nodo2")
    nodo1.agregarSiguiente(nodo2)

    # Al crear nodo3, actualizamos el siguiente de Nodo2
    nodo3 = NodoSimple("Nodo3")
    nodo2.agregarSiguiente(nodo3)

    # Al crear nodo4, actualizamos el siguiente de Nodo3
    nodo4 = NodoSimple("Nodo4")
    nodo3.agregarSiguiente(nodo4)

    # -------------------- Lista circular simple
    print("---------------------- CIRCULAR SIMPLE")
    # Crear nodos
    nodoCircularSimple1 = NodoSimple("Nodo1_C")

    # Al crear nodo2, actualizamos el siguiente de Nodo1, Nodo2
    nodoCircularSimple2 = NodoSimple("Nodo2_C")
    nodoCircularSimple1.agregarSiguiente(nodoCircularSimple2)
    nodoCircularSimple2.agregarSiguiente(nodoCircularSimple1)

    # Al crear nodo3, actualizamos el siguiente de Nodo2, Nodo3
    nodoCircularSimple3 = NodoSimple("Nodo3_C")
    nodoCircularSimple2.agregarSiguiente(nodoCircularSimple3)
    nodoCircularSimple3.agregarSiguiente(nodoCircularSimple1)

    

