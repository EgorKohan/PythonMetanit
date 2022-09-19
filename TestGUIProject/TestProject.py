from tkinter import *

root = Tk()
root.title("GUI Test Project")

people = []

gender_dict = {
    1: "Male",
    2: "Female"
}


class Person:
    def __init__(self, name, surname, gender, is_married):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.is_married = is_married

    def __str__(self):
        return self.name + " " + self.surname


def clear_input(entry):
    def inner(*args):
        entry.delete(0, END)
        entry.unbind("<Button-1>")
        entry.config(foreground="#000")

    return inner


def print_error_in_input(entry, message):
    entry.insert(0, message)
    entry.config(foreground="#D30000")
    entry.bind("<Button-1>", clear_input(entry))


def clear_label(label, btn):
    def inner(*args):
        label.config(foreground="#000")
        btn.unbind("<Button-1>")

    return inner


def highlight_label_if_error(label, radiobuttons):
    label.config(foreground="#D30000")
    for btn in radiobuttons:
        btn.bind("<Button-1>", clear_label(label, btn))


def save():
    name = name_entry.get()
    if name == "":
        print_error_in_input(name_entry, "Name cannot be empty!")
        return
    surname = surname_entry.get()
    if surname == "":
        print_error_in_input(surname_entry, "Surname cannot be empty!")
        return
    gender_var_val = gender_var.get()
    if gender_var_val == 0:
        highlight_label_if_error(gender_label, (male_gender_radiobutton, female_gender_radiobutton))
        return
    gender = gender_dict[gender_var_val]
    is_married = is_married_var.get()
    person = Person(name, surname, gender, is_married)
    people_listbox.insert(END, person)
    person.num_in_listbox = people_listbox.size()
    people.append(person)


def delete():
    people_for_delete = list(people_listbox.curselection())
    people_for_delete.reverse()
    for person_index in people_for_delete:
        people_listbox.delete(person_index)


def print_person_to_show(person, master, start):
    name_label = Label(master, text=f"Name: {person.name}", width=50)
    surname_label = Label(master, text=f"Surname: {person.surname}", width=50)
    gender_label = Label(master, text=f"Gender: {person.gender}", width=50)
    is_married_label = Label(master, text=f"Is married: {person.is_married}", width=50)

    name_label.grid(row=start, column=0, pady=1)
    surname_label.grid(row=start+1, column=0, pady=1)
    gender_label.grid(row=start+2, column=0, pady=1)
    is_married_label.grid(row=start+3, column=0, pady=(1, 10))


def show():
    show_panel = Tk()
    people_to_show = people.copy()

    selected_people = people_listbox.curselection()
    for person_index in selected_people:
        filter(lambda p: p.num_in_listbox == person_index, people_to_show)

    index = 0
    for person in people_to_show:
        print_person_to_show(person, show_panel, index)
        index += 4

    show_panel.mainloop()


name_entry = Entry()
name_label = Label(text="Input name: ")

surname_entry = Entry()
surname_label = Label(text="Input surname: ")

gender_var = IntVar()
gender_label = Label(text="Choose gender: ")
male_gender_radiobutton = Radiobutton(text="Male", value=1, variable=gender_var)
female_gender_radiobutton = Radiobutton(text="Female", value=2, variable=gender_var)

is_married_var = IntVar()
is_married_checkbutton = Checkbutton(text="Married", variable=is_married_var)
is_married_label = Label(text="Are you married?")

people_listbox = Listbox(width=50, height=20, selectmode=MULTIPLE)

save_button = Button(text="Save", command=save)
delete_button = Button(text="Delete", command=delete)
show_button = Button(text="Show", command=show)

people_listbox.grid(
    row=0, column=0,
    rowspan=7, columnspan=2,
    sticky=N + S + W + E,
    padx=(0, 10),
    pady=(0, 10)
)

name_label.grid(
    row=0, column=6,
    padx=3, pady=3
)
name_entry.grid(
    row=0, column=7,
    columnspan=2,
    sticky=W + E
)

surname_label.grid(
    row=1, column=6,
    padx=3, pady=3
)
surname_entry.grid(
    row=1, column=7,
    columnspan=2,
    sticky=W + E
)

gender_label.grid(
    row=2, column=6,
    padx=3, pady=3
)
male_gender_radiobutton.grid(
    row=2, column=7,
    sticky=W
)
female_gender_radiobutton.grid(
    row=2, column=8,
    sticky=W
)

is_married_label.grid(
    row=3, column=6,
    pady=3, padx=3
)
is_married_checkbutton.grid(
    row=3, column=7
)

save_button.grid(
    row=4, column=6, columnspan=3, sticky=W + E, pady=2
)
delete_button.grid(
    row=5, column=6, columnspan=3, sticky=W + E, pady=2
)
show_button.grid(
    row=6, column=6, columnspan=3, sticky=W + E, pady=2
)

root.mainloop()
