from tkinter import *
from tkinter import messagebox

'''
bg: фоновый цвет

bd: толщина границы

cursor: курсор указателя мыши при наведении на текстовое поле

fg: цвет текста

font: шрифт текста

justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю

relief: определяет тип границы, по умолчанию значение FLAT

selectbackground: фоновый цвет выделенного куска текста

selectforeground: цвет выделенного текста

show: задает маску для вводимых символов

state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED

textvariable: устанавливает привязку к элементу StringVar

width: ширина элемента
'''


# def show_message():
#     messagebox.showinfo("GUI on Python", message.get())
#
#
root = Tk()
root.title("GUI on Python")
root.geometry("400x300")
#
# message = StringVar()
# message_entry = Entry(textvariable=message)
# message_entry.place(relx=.5, rely=.1, anchor="center")
#
# message_button = Button(text="Show message", command=show_message)
# message_button.place(relx=.5, rely=.5, anchor="center")
#
# root.mainloop()


def display_full_name():
    messagebox.showinfo("GUI on Python", name.get() + " " + surname.get())


def clear_inputs():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)


name = StringVar()
surname = StringVar()

name_label = Label(text="Input name: ")
surname_label = Label(text="Input surname: ")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.insert(0, "Egor")
surname_entry.insert(0, "Kokhan")

name_label.grid(row=0, column=0, pady=5)
surname_label.grid(row=1, column=0, pady=5)
name_entry.grid(row=0, column=1)
surname_entry.grid(row=1, column=1)

button = Button(text="Click Me", command=display_full_name)
button.grid(row=2, column=1)

clear_button = Button(text="Clear inputs", command=clear_inputs)
clear_button.grid(row=3, column=1)

root.mainloop()