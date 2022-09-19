from tkinter import *

root = Tk()
root.title("GUI on Python")
root.geometry("400x300")
#
# header = Label(text="Choose the course: ", padx=15, pady=10)
# header.grid(row=0, column=0, sticky=W)
#
# lang = IntVar()
#
# python_radiobutton = Radiobutton(text="Python", value=1, variable=lang, pady=10, padx=15)
# python_radiobutton.grid(row=1, column=0, sticky=W)
#
# javascript_radiobutton = Radiobutton(text="JavaScript", value=2, variable=lang, padx=15, pady=10)
# javascript_radiobutton.grid(row=2, column=0, sticky=W)
#
# selection = Label(textvariable=lang, padx=15, pady=10)
# selection.grid(row=3, column=0, sticky=W)
#
# root.mainloop()

'''
activebackground: фоновый цвет переключателя в нажатом состоянии

activeforeground: цвет текста переключателя в нажатом состоянии

bg: фоновый цвет переключателя

bitmap: монохромное изображение для переключателя

borderwidth: граница вокруг переключателя

command: ссылка на функцию, которая вызывается при нажатии на переключатель

cursor: курсор при наведении на элемент

font: шрифт

fg: цвет текста

height: высота элемента в строках текста. По умолчанию равно 1

image: графическое изображение, отображаемое на элементе

justify: выравнивание текста, принимает значения CENTER, LEFT, RIGHT

padx: отступы справа и слева от текста до границы переключателя

pady: отступы сверху и снизу от текста до границы переключателя

relief: стиль переключателя, по умолчанию имеет значение FLAT

selectcolor: цвет кружка переключателя

selectimage: изображение на переключателе, когда он находится в отмеченном состоянии

state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE

text: текст элемента

textvariable: устанавливает привязку к переменной StringVar, которая задает текст переключателя

underline: индекс подчеркнутого символа в тексте элемента

variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние переключателя

value: значение переключателя

width: ширина элемента

wraplength: устанавливает перенос символов на другую строку в тексте элемента
'''

languages = {
    1: "Python",
    2: "Javasript",
    3: "C#",
    4: "Java"
}


def show_choice():
    choice.set(f"Выбран: {languages[radiobutton_var.get()]}")


radiobutton_var = IntVar()
row_num = 0
for language in languages.keys():
    radiobutton = Radiobutton(text=languages[language], command=show_choice, value=language, variable=radiobutton_var)
    radiobutton.grid(row=row_num, column=0, sticky=W)
    row_num += 1

choice = StringVar(value="Ничего не выбрано")
label = Label(textvariable=choice)
label.grid(row=row_num, column=0, sticky=W)

root.mainloop()