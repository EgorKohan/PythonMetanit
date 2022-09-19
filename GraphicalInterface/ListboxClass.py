from tkinter import *

# languages = ["Python", "JavaScript", "C#", "Java"]

root = Tk()
root.title("GUI on Python")
root.geometry("400x300")

# languages_listbox = Listbox()
#
# for language in languages:
#     languages_listbox.insert(END, language)
#
# languages_listbox.pack()
#
# root.mainloop()

'''
bg: фоновый цвет

bd: толщина границы вокруг элемента

cursor: курсор при наведении на Listbox

font: настройки шрифта

fg: цвет текста

height: высота элемента в строках. По умолчанию отображает 10 строк

highlightcolor: цвет элемента, когда он получает фокус

highlightthickness: толщина границы элемента, когда он находится в фокусе

relief: устанавливает стиль элемента, по умолчанию имеет значение SUNKEN

selectbackground: фоновый цвет для выделенного элемента

selectmode: определяет, сколько элементов могут быть выделены. Может принимать следующие значения: BROWSE, SINGLE, MULTIPLE, EXTENDED. Например, если необходимо включить множественное выделение элементов, то можно использовать значения MULTIPLE или EXTENDED.

width: устанавливает ширину элемента в символах. По умолчанию ширина - 20 символов

xscrollcommand: задает горизонтальную прокрутку

yscrollcommand: устанавливает вертикальную прокрутку
'''

# languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
#              "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
#              "T-SQL", "PL-SQL", "Typescript"]
#
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=30)
#
# for language in languages:
#     languages_listbox.insert(END, language)
#
# languages_listbox.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=languages_listbox.yview)
# root.mainloop()

'''
curselection(): возвращает набор индексов выделенных элементов

delete(first, last = None): удаляет элементы с индексами из диапазона [first, last]. Если второй параметр опущен, то удаляет только один элемент по индексу first.

get(first, last = None): возвращает кортеж, который содержит текст элементов с индексами из дипазона [first, last]. Если второй параметр опущен, возвращается только текст элемента с индексом first.

insert(index, element): вставляет элемент по определенному индексу

size(): возвращает количество элементов
'''


def add_element():
    get = input_entry.get()
    if get != "":
        listbox.insert(END, get)
        input_entry.delete(0, END)


def remove_elements():
    curselection = listbox.curselection()
    array = list(curselection)
    array.reverse()
    for index in array:
        listbox.delete(index)


input_entry = Entry(width=40)
add_button = Button(text="Добавить", command=add_element)
listbox = Listbox(width=40, selectmode=MULTIPLE)
remove_button = Button(text="Удалить", command=remove_elements)

input_entry.grid(row=0, column=0, pady=10, padx=10)
add_button.grid(row=0, column=2, pady=10, padx=10)
listbox.grid(row=1, rowspan=4, column=0, columnspan=3, pady=10, padx=10, sticky=W + E)
remove_button.grid(row=5, column=2, pady=10, padx=10)

root.mainloop()
