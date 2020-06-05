from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

root = Tk()
root.title("Calculator")
button_list = [
    "7", "8", "9", "C", "Exit",
    "4", "5", "6", "+", "*",
    "1", "2", "3", "-", "/",
    "0", ".", "=", "xⁿ", "π",
    "sin", "cos", "tg", "1/x", "√x",
    "(", ")", "n!", ]

r = 1
c = 0
for i in button_list:

    cmd = lambda x=i: calc(x)
    btn1 = Button(root, text=i, command=cmd, width=10, background="red")
    btn1.config(bg="blue")
    btn1.grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)


def calc(key):
    global memory
    if key == "=":
        str1 = "-0123456789)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "Exit":
        root.after(1, root.destroy)
        exit(0)
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    elif key == "√x":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    else:
        calc_entry.insert(END, key)


root.mainloop()