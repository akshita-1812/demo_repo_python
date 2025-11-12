# from tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.geometry("500x600+400+50")
# root.title("Calculator")

# def num_btn(num):
#     value = E.get()
#     E.delete(0, END)
#     E.insert(0, str(value) + str(num))

# def add():
#     global oper, add_val
#     add_val = E.get()
#     E.delete(0, END)
#     oper = "+"

# def sub():
#     global oper, sub_val
#     sub_val = E.get()
#     E.delete(0, END)
#     oper = "-"

# def mul():
#     global oper, mul_val
#     mul_val = E.get()
#     E.delete(0, END)
#     oper = "*"

# def div():
#     global oper, div_val
#     div_val = E.get()
#     E.delete(0, END)
#     oper = "/"

# def mod():
#     global oper, mod_val
#     mod_val = E.get()
#     E.delete(0, END)
#     oper = "%"

# def equal():
#     second = E.get()
#     E.delete(0, END)
#     if oper == "+":
#         E.insert(0, int(add_val) + int(second))
#     elif oper == "-":
#         E.insert(0, int(sub_val) - int(second))
#     elif oper == "*":
#         E.insert(0, int(mul_val) * int(second))
#     elif oper == "/":
#         if int(second) == 0:
#             messagebox.showerror("Error", "Division by Zero")
#         else:
#             E.insert(0, int(div_val) / int(second))
#     elif oper == "%":
#         E.insert(0, int(mod_val) % int(second))

# def clear():
#     E.delete(0, END)

# def dell():
#     value = E.get()
#     if value:
#         E.delete(len(value) - 1)

# E = Entry(root, font=("impact", 30), fg="green")
# E.place(x=20, y=20)

# Button(root, text="del", font=("impact", 30), fg="red", width=4, command=dell).place(x=50, y=100)
# Button(root, text="clr", font=("impact", 30), fg="black", width=4, command=clear).place(x=150, y=100)

# Button(root, text="%", font=("impact", 30), fg="black", width=4, command=mod).place(x=250, y=100)
# Button(root, text="/", font=("impact", 30), fg="yellow", width=4, command=div).place(x=350, y=100)

# Button(root, text="7", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(7)).place(x=50, y=200)
# Button(root, text="8", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(8)).place(x=150, y=200)
# Button(root, text="9", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(9)).place(x=250, y=200)
# Button(root, text="*", font=("impact", 30), fg="orange", width=4, command=mul).place(x=350, y=200)

# Button(root, text="4", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(4)).place(x=50, y=300)
# Button(root, text="5", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(5)).place(x=150, y=300)
# Button(root, text="6", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(6)).place(x=250, y=300)
# Button(root, text="-", font=("impact", 30), fg="grey", width=4, command=sub).place(x=350, y=300)

# Button(root, text="1", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(1)).place(x=50, y=400)
# Button(root, text="2", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(2)).place(x=150, y=400)
# Button(root, text="3", font=("impact", 30), fg="black", width=4, command=lambda: num_btn(3)).place(x=250, y=400)
# Button(root, text="+", font=("impact", 30), fg="black", width=4, command=add).place(x=350, y=400)

# Button(root, text="0", font=("impact", 30), fg="black", width=6, command=lambda: num_btn(0)).place(x=50, y=500)
# Button(root, text="=", font=("impact", 30), fg="blue", width=6, command=equal).place(x=250, y=500)

# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.geometry("800x700+200+20")
root.resizable(False, False)
root.title("My Calculator")


calc_frame = tk.Frame(root)
calc_frame.pack(pady=20)


entry = tk.Entry(calc_frame, font=("arial", 24), borderwidth=5, relief="ridge", justify="right", width=15)
entry.grid(row=0, column=0, columnspan=4, pady=10)


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]


for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(calc_frame, text=text, width=5, height=2, bg="#4CAF50", fg="white",
                           font=('Arial', 18), command=calculate)
        button.grid(row=row, column=col, padx=5, pady=5)
    elif text == 'C':
        button = tk.Button(calc_frame, text=text, width=22, height=2, bg="#f44336", fg="white",
                           font=('Arial', 18), command=clear)
        button.grid(row=row, columnspan=4, padx=5, pady=5)
    else:
        button = tk.Button(calc_frame, text=text, width=5, height=2, bg="#e0e0e0",
                           font=('Arial', 18), command=lambda t=text: button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()