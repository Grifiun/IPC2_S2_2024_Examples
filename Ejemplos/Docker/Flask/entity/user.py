
# Entidad de usuario, se usa para crear un objeto usuario
class User:
    def __init__(self, nombre, dpi, correo, edad):
        self.nombre = nombre
        self.dpi = dpi
        self.correo = correo 
        self.edad = edad 

    def to_string(self):
        return f"Nombre: {self.nombre}, DPI: {self.dpi}, correo: {self.correo}, edad: {self.edad}"
    

