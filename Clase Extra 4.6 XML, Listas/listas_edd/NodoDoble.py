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
