from tkinter import Message
from tkinter import *

window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

lbl= Label(text="This application calculates the product of two numbers!", fg="white", bg="purple",height=2,width=300)
lbl_1= Label(text="Please enter the first number",fg="white",bg="light blue", height=2,width=300)
num1=Entry()
lbl_2= Label(text="Please enter the second number",fg="white",bg="light blue", height=2,width=300)
num2=Entry()

def calculate():
    n1=int(num1.get())
    n2=int(num2.get())
    p=n1*n2
    global Message
    Message= "The product is"
    text_box.insert(END,Message)
    text_box.insert(END,p)

text_box= Text(height=3)
btn= Button(text="Calculate",fg="white",bg="dark blue", height=1,command= calculate)

lbl.pack()
lbl_1.pack()
num1.pack()
lbl_2.pack()
num2.pack()
text_box.pack()
btn.pack()

window.mainloop()
