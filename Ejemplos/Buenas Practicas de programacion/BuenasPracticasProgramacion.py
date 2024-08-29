# Ejemplo de nombre de clase en PascalCase
class MiClaseEjemplo:
    
    # Constante en ALL_CAPS
    VALOR_MAXIMO = 100
    
    def __init__(self, nombre, edad):
        # Variables de instancia en snake_case
        self.nombre = nombre
        self.edad = edad
    
    # Método en snake_case
    def mi_metodo_ejemplo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    # Método privado en snake_case con guion bajo inicial
    def _metodo_privado(self):
        print("Este es un método privado.")
    
    # Método fuertemente privado con doble guion bajo inicial
    def __metodo_fuerte_privado(self):
        print("Este es un método fuertemente privado.")

# Uso de la clase
objeto = MiClaseEjemplo("Juan", 30)
objeto.mi_metodo_ejemplo()
