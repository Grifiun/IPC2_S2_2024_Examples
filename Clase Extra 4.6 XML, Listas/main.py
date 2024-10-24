from listas_edd.NodoSimple import NodoSimple

def main():
    # PRUEBA LISTA SIMPLE

    # Crear nodos
    nodo1 = NodoSimple("Nodo1")

    # Al crear nodo2, actualizamos el siguiente de Nodo1
    nodo2 = NodoSimple("Nodo2")
    nodo1.agregarSiguiente(nodo2)
    nodo2.agregarSiguiente(nodo1)

    # Al crear nodo3, actualizamos el siguiente de Nodo2
    nodo3 = NodoSimple("Nodo3")
    nodo3.agregarSiguiente(nodo1)
    nodo2.agregarSiguiente(nodo3)

    # Al crear nodo4, actualizamos el siguiente de Nodo3
    nodo4 = NodoSimple("Nodo4")    
    nodo3.agregarSiguiente(nodo4)
    nodo4.agregarSiguiente(nodo1)

    # --------------- RECORRER
    print("------------------ RECORRER CICLO CON WHILE")
    nodoIncial = nodo1
    nodoIter = nodoIncial
    while nodoIter != None:
        nodoIter.imprimirTexto()
        if (nodoIter.siguiente == nodoIncial):
            break
        nodoIter = nodoIter.siguiente

    # --------------- RECORRER CON FUNCION ITERADOR
    print("------------------ RECORRER CICLO FOR")
    for elementoNodo in nodo1:
        elementoNodo.imprimirTexto()
        if elementoNodo.siguiente == nodo1:
            break    

if __name__ == "__main__":
    main()
