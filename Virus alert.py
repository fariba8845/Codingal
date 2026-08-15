import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.geometry("200x200")
root.title("Alerts")

def msg():
    messagebox.showwarning("Alert","STop! Virus detected")

button= tk.Button(root, text="Scan Virus",command=msg)
button.place(x=40,y=80)

root.mainloop()