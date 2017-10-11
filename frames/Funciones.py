import tkinter as tk
from tkinter import ttk
import serial


class Funciones(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Variables to hold values
        selectedFunction = tk.StringVar()

        # CheckButtons
        senoRadioButton = tk.Radiobutton(self, text="Seno", variable=selectedFunction, value="SEN")
        cosenoRadioButton = tk.Radiobutton(self, text="Cuadrada", variable=selectedFunction, value="CUA")
        triangularRadioButton = tk.Radiobutton(self, text="Triangular", variable=selectedFunction, value="TRI")
        rampaRadioButton = tk.Radiobutton(self, text="Rampa", variable=selectedFunction, value="RAM")

        # Spinners
        frequencySpinner = tk.Spinbox(self, from_=10, to=50000, increment=1)
        amplitudeSpinner = tk.Spinbox(self, from_=0, to=5, increment=1)

        # Labels
        label = tk.Label(self, text="Generador de Funciones").grid(row=0, column=3)
        label = tk.Label(self, text="Frecuencia Hz 10-50000").grid(row=4, column=2, pady=(40,0))
        label = tk.Label(self, text="Amplitud Hz 0-5").grid(row=4, column=4, pady=(40,0))

        # Buttons
        buttonHome = tk.Button(self, text="Inicio",
                            command=lambda: controller.show_frame("HomeFrame"))
        buttonIniciar = tk.Button(self, text="Comenzar",
                                  command=lambda: self.iniciarFuncion(selectedFunction.get() + "#F#" +
                                                                      frequencySpinner.get()+ "#A#" +
                                                                      amplitudeSpinner.get()))

        senoRadioButton.grid(row=2, column=2, pady=20, padx= 50)
        cosenoRadioButton.grid(row=2, column=4)
        triangularRadioButton.grid(row=3, column=2)
        rampaRadioButton.grid(row=3, column=4)
        frequencySpinner.grid(row=5, column=2, padx=(20,0))
        amplitudeSpinner.grid(row=5, column=4, padx=(20,0))
        buttonHome.grid(row=1, column=3, padx=(20,0))
        buttonIniciar.grid(row=6, column=3, pady=(20,0), padx=(20,0))

    def iniciarFuncion(self, message):
        # ser = serial.Serial('COM4', 115200, timeout=3)
        # ser.close()
        # ser.open()
        # ser.write(message)

        print(message)
