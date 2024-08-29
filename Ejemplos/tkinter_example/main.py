import tkinter as tk
from tkinter_materials.window import Window
from tkinter_materials.button import Button
from tkinter_materials.texto import Texto
# from window import Window

# Clase principal que utiliza las otras clases
class Main:
    def __init__(self, width = 600, height = 700):
        self.window = Window(title="Demo de Tkinter", width=width, height=height)
        self.label = Texto(self.window.get_root(), text="Presiona un botón para empezar", x=100, y=50)
        self.button_in_air = None

        # Botones
        self.button1 = Button(self.window.get_root(), text="Botón 1", command=self.boton1_funcion, x=200, y=100)
        self.button2 = Button(self.window.get_root(), text="Botón 2", command=self.boton2_funcion, x=300, y=100)
        self.button3 = Button(self.window.get_root(), text="Botón 3", x=width/2, y=200)
        self.button4 = Button(self.window.get_root(), text="Botón 4", x=width/2, y=250)

        # Asignar comandos después de la inicialización
        self.button3.set_command(lambda: self.boton_air(self.button3))
        self.button4.set_command(lambda: self.boton_air(self.button4))

    def boton1_funcion(self):
        self.label.set_text("¡Botón 1 presionado!")

    def boton2_funcion(self):
        self.label.set_text("¡Botón 2 presionado!")

    def boton_air(self, button):
        posicion_mover = (300, 500)

        if self.button_in_air is None:
            # Si no hay botón en el aire, mover el botón a (300, 300)
            self.button_in_air = button
            self.button_in_air.move(*posicion_mover)
        else:
            # Si ya hay un botón en el aire
            if self.button_in_air == button:
                # Si es el mismo botón, volver a su posición original
                self.button_in_air.reset_position()
                self.button_in_air = None
            else:
                # Si es otro botón, devolver el botón anterior a su posición original
                self.button_in_air.reset_position()
                # Y mover el nuevo botón a (300, 300)
                self.button_in_air = button
                self.button_in_air.move(*posicion_mover)

    def run(self):
        self.window.run()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = Main()
    app.run()
