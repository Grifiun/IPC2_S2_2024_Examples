class Estudiante:
    def __init__(self, carnet, nombre, year, creditos):
        self.carnet = carnet
        self.nombre = nombre
        self.year = year
        self.creditos = creditos

    def imprimirEstudiante(self):
        print(f"Estudiante {self.nombre} con carne {self.carnet}, inscrito en {self.year} tiene {self.creditos} creditos.")

    # tienen carné, cantidad créditos, año de inscripción, nombre completo…    

