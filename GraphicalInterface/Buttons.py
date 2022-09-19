from tkinter import *

root = Tk()
root.title("GUI on Python")
root.geometry("300x250")


def click_btn():
    clicks = 0

    def inner():
        nonlocal clicks
        clicks += 1
        root.title(f"Clicks: {clicks}")

    return inner


btn = Button(
    text="Hello",
    background="#555",
    activebackground="#555",
    highlightcolor="#555",
    foreground="#ccc",
    padx="20",
    pady="8",
    font="16",
    command=click_btn()
)
btn.pack()

root.mainloop()

'''
activebackground: цвет кнопки, когда она находится в нажатом состоянии

activeforeground: цвет текста кнопки, когда она в нажатом состоянии

bd: толщина границы (по умолчанию 2)

bg/background: фоновый цвет кнопки

fg/foreground: цвет текста кнопки

font: шрифт текста, например, font="Arial 14" - шрифт Arial высотой 14px, или font=("Verdana", 13, "bold") - шрифт Verdana высотой 13px с выделением жирным

height: высота кнопки

highlightcolor: цвет кнопки, когда она в фокусе

image: изображение на кнопке

justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю

padx: отступ от границ кнопки до ее текста справа и слева

pady: отступ от границ кнопки до ее текста сверху и снизу

relief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE

state: устанавливает состояние кнопки, может принимать значения DISABLED, ACTIVE, NORMAL (по умолчанию)

text: устанавливает текст кнопки

textvariable: устанавливает привязку к элементу StringVar

underline: указывает на номер символа в тексте кнопки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается

width: ширина кнопки

wraplength: при положительном значении строки текста будут переносится для вмещения в пространство кнопки
'''