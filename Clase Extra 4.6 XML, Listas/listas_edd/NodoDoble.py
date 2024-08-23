from NodoSimple import NodoSimple

class NodoDoble(NodoSimple):
    def __init__(self, texto):
        super().__init__(texto)
        self.anterior = None

    def agregarAnterior(self, nodo):
        self.anterior = nodo
        print(f"{nodo.texto} <- anterior <- {self.texto}")

if __name__ == "__main__":
    print("Ejecutando Main de NodoDoble")

    # Crear nodos
    nodo1 = NodoDoble("Nodo1")

    # Al crear nodo2, actualizamos el siguiente de Nodo1
    nodo2 = NodoDoble("Nodo2")
    nodo1.agregarSiguiente(nodo2)
    nodo2.agregarAnterior(nodo1)

    # Al crear nodo3, actualizamos el siguiente de Nodo2
    nodo3 = NodoDoble("Nodo3")
    nodo2.agregarSiguiente(nodo3)
    nodo3.agregarAnterior(nodo2)

    # Al crear nodo4, actualizamos el siguiente de Nodo3
    nodo4 = NodoDoble("Nodo4")
    nodo3.agregarSiguiente(nodo4)
    nodo4.agregarAnterior(nodo3)

    # -------------------- Lista circular doble enlace
    print("---------------------- CIRCULAR DOBLE ENLACE")
    # Crear nodos
    nodoCircularSimple1 = NodoDoble("Nodo1_CD")

    # Al crear nodo2, actualizamos el siguiente de Nodo1, Nodo2; anterior nodo1, nodo2
    nodoCircularSimple2 = NodoDoble("Nodo2_CD")
    nodoCircularSimple1.agregarSiguiente(nodoCircularSimple2)
    nodoCircularSimple2.agregarSiguiente(nodoCircularSimple1)

    nodoCircularSimple2.agregarAnterior(nodoCircularSimple1)
    nodoCircularSimple1.agregarAnterior(nodoCircularSimple2)    

    # Al crear nodo2, actualizamos el siguiente de Nodo2, Nodo3; anterior nodo1, nodo2
    nodoCircularSimple3 = NodoDoble("Nodo3_CD")
    nodoCircularSimple2.agregarSiguiente(nodoCircularSimple2)
    nodoCircularSimple3.agregarSiguiente(nodoCircularSimple1)

    nodoCircularSimple3.agregarAnterior(nodoCircularSimple2)
    nodoCircularSimple1.agregarAnterior(nodoCircularSimple3)
    
