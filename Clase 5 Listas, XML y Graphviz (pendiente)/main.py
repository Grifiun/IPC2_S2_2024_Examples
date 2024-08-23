from listas_edd.NodoEstudiante import NodoEstudiante
from dao.Estudiante import Estudiante

def main():
    # PRUEBA LISTA SIMPLE

    # Crear nodos    
    nodoEstudiante1 = NodoEstudiante(1, Estudiante("200020200", "Juan", "2000", "250"))
    nodoEstudiante2 = NodoEstudiante(2, Estudiante("200120200", "Pedro", "2001", "250"))
    nodoEstudiante3 = NodoEstudiante(3, Estudiante("200220200", "Maria", "2002", "250"))
    nodoEstudiante4 = NodoEstudiante(4, Estudiante("200320200", "Jose Maria", "2003", "250"))
    nodoEstudiante5 = NodoEstudiante(5, Estudiante("200420200", "Maria Jose", "2004", "250"))

    # Enlaces
    nodoEstudiante1.agregarSiguiente(nodoEstudiante2)
    nodoEstudiante2.agregarSiguiente(nodoEstudiante3)
    nodoEstudiante3.agregarSiguiente(nodoEstudiante4)
    nodoEstudiante4.agregarSiguiente(nodoEstudiante5)
    nodoEstudiante5.agregarSiguiente(nodoEstudiante1)

    # --------------- RECORRER CON FUNCION ITERADOR
    print("------------------ RECORRER CICLO FOR")
    nodoInicial = nodoEstudiante1
    for nodoEstudianteAuxiliar in nodoEstudiante1:
        estudianteAux = nodoEstudianteAuxiliar.estudiante
        estudianteAux.imprimirEstudiante()
        if nodoEstudianteAuxiliar.siguiente == nodoInicial:
            break    

if __name__ == "__main__":
    main()
