import tkinter as tk

# Clase que crea la ventana principal
class Window:
    def __init__(self, title="Ventana", width=300, height=300):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

    def get_root(self):
        return self.root

    def run(self):
        self.root.mainloop()