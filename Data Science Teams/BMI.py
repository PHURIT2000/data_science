import tkinter as tk
from tkinter import *
def CalculateBMI(height, weight):
    hm = height/100
    bmi = weight/(hm**2)
    display_t = checkBMI(bmi) 
    display_v.set(display_t)  
    return format(bmi, '.2f')
    
    

def checkBMI(vars): 
    if vars < 18.5:
        return str("Your Underweight")
    elif vars >= 18.5 and vars < 25:
        return str("Your Healthy")
    elif vars >= 25 and vars < 30:
        return str("Your Overweight")
    elif vars > 30:
        return str("Your Severely Overweight")
    else:
        return str("Error")
def on_click():
    bmi_g = CalculateBMI(hm_cm.get(), wg_kg.get())
    bmi_s.set(bmi_g)
    ##display_v = checkBMI(bmi_g)
    ##display_v.set(display_t)


root = tk.Tk()
root.option_add("*Font", "impact 30")
hm_cm = DoubleVar()
wg_kg = DoubleVar()
bmi_s = DoubleVar()
display_v = StringVar()
Entry(root, textvariable=hm_cm, justify="right").grid(row=0, column=0)
Label(root, text="cm.").grid(row=0, column=1)
Entry(root, textvariable=wg_kg, justify="right").grid(row=1, column=0)
Label(root, text="kg.").grid(row=1, column=1)
Button(root, text=" Submit ", command=on_click).grid(row=4, column=0, sticky=S)
Label(root, text="BMI ").grid(row=2, column=0)
Label(root, textvariable=bmi_s).grid(row=2, column=1)
Label(root, textvariable=display_v).grid(row=3, column=0)
root.mainloop()