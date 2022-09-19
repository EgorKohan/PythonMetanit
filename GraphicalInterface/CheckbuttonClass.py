from tkinter import *

'''
activebackground: фоновый цвет флажка в нажатом состоянии

activeforeground: цвет текста флажка в нажатом состоянии

bg: фоновый цвет флажка

bitmap: монохромное изображение для флажка

bd: граница вокруг флажка

command: ссылка на функцию, которая вызывается при нажатии на флажок

cursor: курсор при наведении на элемент

disabledforeground: цвет текста в состоянии DISABLED

font: шрифт

fg: цвет текста

height: высота элемента

image: графическое изображение, отображаемое на элементе

justify: выравнивание текста, принимает значения CENTER, LEFT, RIGHT

offvalue: значение ассоциированной с флажком переменной IntVar в неотмеченном состоянии, по умолчанию равно 0

onvalue: значение ассоциированной с флажком переменной IntVar в отмеченном состоянии, по умолчанию равно 1

padx: отступы справа и слева от текста до границы флажка

pady: отступы сверху и снизу от текста до границы флажка

relief: стиль флажка, по умолчанию имеет значение FLAT

selectcolor: цвет квадратика флажка

selectimage: изображение на флажке, когда он находится в отмеченном состоянии

state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE

text: текст элемента

underline: индекс подчеркнутого символа в тексте флажка

variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние флажка

width: ширина элемента

wraplength: устанавливает перенос символов на другую строку в тексте элемента
'''

# root = Tk()
# root.title("GUI on Python")
# root.geometry("400x300")
#
# is_married = IntVar()
#
# is_married_checkbutton = Checkbutton(text="Женат/Замужем", variable=is_married)
# is_married_checkbutton.pack()
#
# is_married_label = Label(textvariable=is_married)
# is_married_label.place(relx=.5, rely=.5, anchor="center")
#
# root.mainloop()

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")


def show_language():
    mass = []
    global text_var
    if python_lang.get() == 1:
        mass.append("Python")
    if javascript_lang.get() == 1:
        mass.append("JavaScript")
    text_var.set(", ".join(mass))


python_lang = IntVar()
python_checkbutton = Checkbutton(text="Python", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10, command=show_language)
python_checkbutton.grid(row=0, column=0, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="JavaScript", variable=javascript_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10, command=show_language)
javascript_checkbutton.grid(row=1, column=0, sticky=W)

text_var = StringVar(value="Hello")
label = Label(textvariable=text_var)
label.grid(row=2, column=0, sticky=W)

root.mainloop()
