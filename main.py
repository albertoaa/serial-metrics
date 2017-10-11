import tkinter as tk
from frames.HomeFrame import HomeFrame
from frames.Multimetro import Multimetro
from frames.Funciones import Funciones

class SerialMetrics(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "Serial Metrics")
        tk.Tk.iconbitmap(self, '@/home/albertoaa/workspace/python-projects/serialMetrics/icons/icon.xbm')
        tk.Tk.resizable(self, width=False, height=False)
        tk.Tk.geometry(self, '{}x{}'.format(600, 400))

        # Icon for Windows OS
        # tk.Tk.iconbitmap(self, 'icons/icon.ico')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomeFrame, Multimetro, Funciones):
            page_name = F.__name__
            frame = F(container, self)

            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomeFrame")

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

app = SerialMetrics()
app.mainloop()