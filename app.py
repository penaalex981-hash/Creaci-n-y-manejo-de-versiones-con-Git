import tkinter as tk
from tkinter import ttk

class Main():
    def __init__(self, root):
        self.root=root
        self.root.title("Registero de actividades")
        self.root.geometry("800*800")
        self.crear_widgets()


    ventana=tk.Tk()
   
    ventana.mainloop()