import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("600x500")
root.title("simple calculator")

calci = ttk.Frame(root,padding='50 50 50 50')
calci.pack()

l1 =ttk.Label(calci,text="Enter first no -")
l1.grid(column=0,row=0)

n1=tk.StringVar()
ttk.Entry(calci,width=25,textvariable=n1).grid(column=1,row=0)

l2 = ttk.Label(calci,text="Enter second number - ").grid(column=0,row=1)
n2=tk.StringVar()
ttk.Entry(calci,width=25,textvariable=n2).grid(column=1,row=1)

def add():
    num1 = float(n1.get())
    num2 = float(n2.get())
    res.set(num1+num2)
def sub():
    num1 = float(n1.get())
    num2 = float(n2.get())
    res.set(num1 - num2)
def mul():
    num1 = float(n1.get())
    num2 = float(n2.get())
    res.set(num1*num2)
def div():
    num1 = float(n1.get())
    num2 = float(n2.get())
    if num2==0:
        res.set("Divide by zero error")
    else:
        res.set(num1/num2)

ttk.Button(calci,text="Add",command=add).grid(column=0,row=2)
ttk.Button(calci,text="Sub",command=sub).grid(column=1,row=2)
ttk.Button(calci,text="Mul",command=mul).grid(column=0,row=3)
ttk.Button(calci,text="Div",command=div).grid(column=1,row=3)
res=tk.StringVar()
l3=ttk.Label(calci,text="Result - ").grid(column=0,row=4)
ttk.Entry(calci,width=30,textvariable=res,state='readonly').grid(column=1,row=4)

for child in calci.winfo_children():
    child.grid_configure(padx=5,pady=5)
root.mainloop()