import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.geometry("350x600")
root.title("Routine checker")
root.config(background="light blue")

def check_box():
    if textbox1.get("1.0","end").strip()== "":
        messagebox.showwarning("Empty list","Please enter tasks")
    else:
        messagebox.showinfo("Routine","Great job!")

label1= tk.Label(
    root,
    text="Routine Checker",
    background="light blue",
    fg="white",
    font=("Arial",32,"bold")
)
label1.place(x=20,y=10)

label2= tk.Label(
    root,
    text="Enter your task:",
    fg="white",
    background="light blue",
    font=("Arial",16)
)
label2.place(x=20, y=60)


entry1 = tk.Entry(root)
entry1.place(x=20,y=90)

label3= tk.Label(
    root,
    text="",
    fg="white",
    background="light blue",
    font=("Arial",16)
)
label3.place(x=20, y=120)


button1= tk.Button(
    root,
    text="Add task",
    fg="white",
    background="navy blue",
    font=("Arial",16)
)
button1.place(x=20, y=150)

textbox1= tk.Text(
    root,
    fg="white",
    background="light blue",
    font=("Arial",16)
)
textbox1.place(x=20, y=180)

button2= tk.Button(
    root,
    command=check_box,
    text="Check My Routine",
    fg="white",
    background="navy blue",
    font=("Arial",16)
)
button2.place(x=20, y=400)

def handle_keypress(event):
    label3.config(text="Last key pressed:"+event.char)
root.bind("<KeyPress>",handle_keypress)

def handle_click(event):
    textbox1.insert("end", entry1.get() + "\n")
    entry1.delete(0,"END")

button1.bind("<Button-1>",handle_click)

root.mainloop()
