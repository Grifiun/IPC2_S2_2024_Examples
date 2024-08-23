from dao.Estudiante import Estudiante

class NodoEstudiante:
    def __init__(self, id, estudiante):
        print(f"Se creo nodo")
        self.id = id
        self.estudiante = estudiante
        self.siguiente = None

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            nodo_actual = self.current
            self.current = self.current.siguiente              
            return nodo_actual 

    def agregarSiguiente(self, nodo):
        self.siguiente = nodo

