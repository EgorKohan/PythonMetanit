from tkinter import *
from tkinter import messagebox

'''
add_command(options): добавляет элемент меню через параметр options

add_cascade(options): добавляет элемент меню, который в свою очередь может представлять подменю

add_separator(): добавляет линию-разграничитель

add_radiobutton(options): добавляет в меню переключатель

add_checkbutton(options): добавляет в меню флажок
'''


def edit_click():
    messagebox.showinfo("GUI on Python", "Нажата опция Edit")


root = Tk()
root.title("GUI on Python")
root.geometry("400x300")

file_menu = Menu(font=("Verdand", 10, "bold"), tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu = Menu()
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View")


root.config(menu=main_menu)
root.mainloop()

'''
activebackground: цвет активного пункта меню

activeborderwidth: толщина границы активного пункта меню

activeforeground: цвет текста активного пункта меню

bg: фоновый цвет

bd: толщина границы

cursor: курсор указателя мыши при наведении на меню

disabledforeground: цвет, когда меню находится в состоянии DISABLED

font: шрифт текста

fg: цвет текста

tearoff: меню может быть отсоединено от графического окна. В частности, при создании подменю а скриншоте можно 
увидеть прерывающуюся линию в верху подменю, за которую его можно отсоединить. Однако при значении tearoff=0 
подменю не сможет быть отсоединено.
'''