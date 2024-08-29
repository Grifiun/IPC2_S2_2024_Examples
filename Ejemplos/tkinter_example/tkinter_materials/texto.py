import tkinter as tk

# Clase que crea un texto (label)
class Texto:
    def __init__(self, window, text, x=0, y=0):
        self.label = tk.Label(window, text=text)
        self.label.place(x=x, y=y)

    def set_text(self, text):
        self.label.config(text=text)