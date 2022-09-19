from tkinter import *

clicks = 0

root = Tk()
root.title("GUI on Python")
root.geometry("400x300")

btn = Button(
    text="Click me",
    background="#555",
    font="35"
)

# btn.pack(fill=BOTH, expand=True)

btn1 = Button(
    text="Btn 1",
    background="#555"
)

btn2 = Button(
    text="Btn 2",
    background="#555"
)

btn3 = Button(
    text="Btn 3",
    background="#555"
)

btn4 = Button(
    text="Btn 4",
    background="#555"
)

# btn1.pack(side=LEFT, fill=Y)
# btn2.pack(side=TOP, fill=X)
# btn3.pack(side=RIGHT)
# btn4.pack(side=BOTTOM)

clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn5.config(text=f"Clicks: {clicks}")


btn5 = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)


# btn5.place(
#     relx=.5,
#     rely=.5,
#     # relx=.5,
#     # rely=.5,
#     # anchor="center",
#     relheight=.2,
#     relwidth=.2
#     # bordermode=OUTSIDE
# )

btn6 = Button(
    text="Button6", background="#555", foreground="#ccc", padx="14", pady="7", font="13"
)

btn7 = Button(
    text="Button7", background="#555", foreground="#ccc", padx="14", pady="7", font="13"
)
btn8 = Button(
    text="Button8", background="#555", foreground="#ccc", padx="14", pady="7", font="13"
)

btn6.place(
    x=10, y=20
)
btn7.place(
    x=50, y=100
)
btn8.place(
    x=140, y=160
)

root.mainloop()