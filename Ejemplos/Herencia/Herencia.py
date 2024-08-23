class Animal:
    def __init__(self, esta_vivo):
        self._esta_vivo = esta_vivo

    def respirar(self):
        print("El animal está respirando")

    def hacer_ruido(self):
        print("Sonido animal")

class Gato(Animal):
    def __init__(self, esta_vivo, colores, sonido, nombre, tiene_hambre, foto):
        super().__init__(esta_vivo)
        self._colores = colores
        self._sonido = sonido
        self.nombre = nombre
        self.tiene_hambre = tiene_hambre
        self.foto = foto

class Perro(Animal):
    def __init__(self, esta_vivo, colores, sonido, nombre):
        super().__init__(esta_vivo)
        self.esta_vivo = esta_vivo
        self.colores = colores
        self.sonido = sonido
        self.nombre = nombre
    
    def hacer_ruido(self):
        print("El perro esta diciendo: " + self.sonido)

############### INSTANCIAS
# Instancia gato1
gato1 = Gato(esta_vivo=True, colores=['blanco', 'negro'], sonido='miau', nombre='Beluga', tiene_hambre=True, foto=None)
gato1.respirar()
gato1.hacer_ruido()    


perro1 = Perro(esta_vivo=True, colores=['blanco', 'negro'], sonido='guau', nombre='Beluga')
perro1.respirar()
perro1.hacer_ruido()
    

