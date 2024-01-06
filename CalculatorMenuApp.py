import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from GraphingCalculator import Grapher 
from GradeCalculator import Calculator

class HomeMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button_calculator = tk.Button(self, text="Class Grade Calculator", command=self.open_calculator)
        self.button_calculator.pack()

        self.button_grapher = tk.Button(self, text="Function Grapher", command=self.open_grapher)
        self.button_grapher.pack()

    def open_calculator(self):
        self.destroy()  
        CalculatorMenu(self.master)

    def open_grapher(self):
        self.destroy() 
        GrapherMenu(self.master)

class CalculatorMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        calculator = Calculator(self)
        calculator.pack()

        back_button = tk.Button(self, text="Back to Home", command=self.back_to_home)
        back_button.pack()

    def back_to_home(self):
        self.destroy()  
        HomeMenu(self.master)

class GrapherMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        grapher = Grapher(self)
        grapher.pack()

        back_button = tk.Button(self, text="Back to Home", command=self.back_to_home)
        back_button.pack()

    def back_to_home(self):
        self.destroy()  
        HomeMenu(self.master)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Home Menu")
    home_menu = HomeMenu(master=root)
    root.mainloop()
