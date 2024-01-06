import tkinter as tk
import sys
from pathlib import Path

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
        self.destroy()  # Close the current menu
        exec_script("GradeCalculator.py")

    def open_grapher(self):
        self.destroy()  # Close the current menu
        exec_script("GraphingCalculator.py")

def exec_script(script_filename):
    script_path = Path(__file__).parent / script_filename
    try:
        exec(open(script_path).read(), globals())
    except Exception as e:
        print(f"Error executing {script_filename}: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Home Menu")
    home_menu = HomeMenu(master=root)
    root.mainloop()