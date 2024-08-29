import tkinter as tk

# Clase que crea botones
class Button:
    def __init__(self, window, text, command=None, x=0, y=0):
        self.button = tk.Button(window, text=text, command=command)
        self.button.place(x=x, y=y)
        self.original_position = (x, y)

    def set_command(self, command):
        self.button.config(command=command)

    def move(self, x, y):
        self.button.place(x=x, y=y)

    def reset_position(self):
        self.move(*self.original_position)