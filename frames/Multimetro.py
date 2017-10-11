import tkinter as tk


class Multimetro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Multimetro")
        label.pack(pady=10, padx=10)

        buttonHome = tk.Button(self, text="Inicio",
                            command=lambda: controller.show_frame("HomeFrame"))
        buttonHome.pack()

