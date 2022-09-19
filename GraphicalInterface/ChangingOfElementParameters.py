from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    buttonText.set(f"Clicks: {clicks}")


root = Tk()
root.title("GUI on Python")
root.geometry("400x300")

buttonText = StringVar()
buttonText.set(f"Clicks: {clicks}")

btn = Button(
    root,
    textvariable=buttonText,
    background="#555",
    foreground="#ccc",
    padx="20",
    pady="8",
    font="16",
    command=click_button
)


def click_int_button():
    global clicks
    intText.set(clicks)
    clicks += 1


intText = IntVar()

btn2 = Button(
    root,
    textvariable=intText,
    background="#777",
    foreground="#bbb",
    padx="20",
    pady="8",
    font="16",
    command=click_int_button
)


def click_button_config():
    global clicks
    clicks += 1
    btn3.config(text=f"Clicks: {clicks}")


btn3 = Button(
    root,
    text="-",
    background="#777",
    foreground="#bbb",
    padx="20",
    pady="8",
    font="16",
    command=click_button_config
)


btn.pack()
btn2.pack()
btn3.pack()

root.mainloop()