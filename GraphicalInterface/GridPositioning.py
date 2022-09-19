from tkinter import *

root = Tk()
root.title("Grid in Python")
root.geometry("500x400")

number = ""


def add_digit_to_number(digit):
    def inner():
        global number
        number += str(digit)
        label.config(text=number)

    return inner


for i in range(3):
    for j in range(3):
        btn = Button(
            text=str(i + j + 2 * i + 1)
        )
        btn.config(
            command=add_digit_to_number(i + j + 2 * i + 1)
        )
        btn.grid(
            column=j,
            row=i,
            padx=10,
            pady=10
        )

label = Label(text="Hello")
label.grid(
    row=3,
    columnspan=3
)


def clear_label():
    label.config(text="")
    global number
    number = ""


clear_btn = Button(text="Clear", command=clear_label)

clear_btn.grid(
    row=4,
    column=1
)

root.mainloop()
