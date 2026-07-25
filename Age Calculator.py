from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator")
root.geometry("450x400")

# Frame
frm = Frame(master=root, bg="light blue", padx=20, pady=20)
frm.pack()

# Labels
lbl = Label(frm, text="Calculate Your Age!",
            bg="blue", fg="white",
            width=20, height=2,
            font=("Calibri", 20, "bold"))

lbl1 = Label(frm, text="Enter your name", bg="light blue")
lbl2 = Label(frm, text="Enter your birth year", bg="light blue")
lbl3 = Label(frm, text="Enter your birth month", bg="light blue")
lbl4 = Label(frm, text="Enter your birth day", bg="light blue")

# Entries
name_entry = Entry(frm, width=20)
year_entry = Entry(frm, width=20)
month_entry = Entry(frm, width=20)
day_entry = Entry(frm, width=20)

# Text box
text_box = Text(frm, width=35, height=4)

def display():
    person_name = name_entry.get()

    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())

    today = date.today()
    birthday = date(year, month, day)

    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    message ="Hey, "+ person_name+"\nYou are "+ str(age) +" years old"

    text_box.insert(END, message)

# Button
btn = Button(master=frm,
             text="Calculate Age",
             bg="blue",
             fg="white",
             width=20,
             height=2,
             command=display)

# Grid Layout
lbl.grid(row=0, column=0, columnspan=2, pady=10)

lbl1.grid(row=1, column=0, padx=5, pady=5)
name_entry.grid(row=1, column=1, padx=5, pady=5)

lbl2.grid(row=2, column=0, padx=5, pady=5)
year_entry.grid(row=2, column=1, padx=5, pady=5)

lbl3.grid(row=3, column=0, padx=5, pady=5)
month_entry.grid(row=3, column=1, padx=5, pady=5)

lbl4.grid(row=4, column=0, padx=5, pady=5)
day_entry.grid(row=4, column=1, padx=5, pady=5)

btn.grid(row=5, column=0, columnspan=2, pady=15)

text_box.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()