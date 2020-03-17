import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

class check:
    def __init__(self, option):
        self.option = option
    def checkOption(self, vars): 
        self.text1 = ' '
        self.text2 = ' '
        if vars == 'Circumference':
            self.text1 = 'รัศมี'
            self.text2 = ' '
        elif vars == 'Square Area':
            self.text1 = 'ความยาวของด้าน'
            self.text2 = ' '
        elif vars == 'Triangle Area':
            self.text1 = 'ความยาวฐาน'
            self.text2 = 'ความสูง'
        elif vars == 'Circle Area':
            self.text1 = 'รัสมีของวงกลม'
            self.text2 = ' '
        else:
            return str("Error")
class calculate:
    def __init__(self, option):
        self.option = option
    def Answer(self, vars): 
        if vars == 'Circumference':
            return circumference(value1.get())
        elif vars == 'Square Area':
            return calculate_square_area(value1.get())
        elif vars == 'Triangle Area':
            return calculate_triangle_area(value1.get(), value2.get())
        elif vars == 'Circle Area':
            return calculate_circle_area(value1.get())
        else:
            return str("Error")
def circumference(d):
     circumference = 2*(math.pi*d)
     return circumference 
def calculate_square_area(d):
     square_area = d * d
     return square_area
def calculate_triangle_area(b, h):
     triangle_area = (1.0/2.0) * b * h
     return triangle_area
def calculate_circle_area(r):
     circle_area = math.pi * r * r
     return circle_area 
def on_click():
    Option_Selec.checkOption(option_s.get())
    Entry(root, textvariable=value1, justify="right").grid(row=2, column=0)
    Label(root, text=Option_Selec.text1).grid(row=2, column=1)
    Entry(root, textvariable=value2, justify="right").grid(row=3, column=0)
    Label(root, text=Option_Selec.text2).grid(row=3, column=1)
    Button(root, text=' Submit ', command=on_clicksubmit).grid(row=4, column=0)
  
root = tk.Tk()
root.option_add("*Font", "consolas 25")
option_s = ttk.Combobox(root, values=['Circumference','Square Area','Triangle Area','Circle Area'])
value1 = DoubleVar()
value2 = DoubleVar()
gg = DoubleVar()
Option_Selec = check(option_s.get())
option_s.grid(row=1, column=0)
Button(root, text=' Select ', command=on_click).grid(row=1, column=1)
def on_clicksubmit():
    fanal = calculate(option_s.get()) 
    print(fanal.Answer(option_s.get()))
    gg.set(fanal.Answer(option_s.get()))
    Label(root, text='Answer').grid(row=5, column=0)
    Label(root, textvariable=gg).grid(row=5, column=1)  

root.mainloop()