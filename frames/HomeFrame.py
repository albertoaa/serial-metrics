import tkinter as tk


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.grid(self, row=0, column=0, rowspan=3, columnspan=3, sticky="NSEW")
        label = tk.Label(self, text="Inicio")
        label.pack(pady=10, padx=10)

        buttonMultimetro = tk.Button(self, height=5, width=20, text="Multimetro",
                            command=lambda: controller.show_frame("Multimetro"))
        buttonMultimetro.pack()

        buttonFunciones = tk.Button(self, height=5, width=20, text="Funciones",
                            command=lambda: controller.show_frame("Funciones"))
        buttonFunciones.pack()

        buttonOsciloscopio = tk.Button(self, height=5, width=20, text="Osciloscopio",
                            command=lambda: controller.show_frame("Multimetro"))
        buttonOsciloscopio.pack()

        label = tk.Label(self, text="Copyright 2017")
        label.pack(pady=30, padx=10)
