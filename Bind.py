import tkinter as tk

root= tk.Tk()
root.geometry("100x100")
root.title("Event handeler")

def handel_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

root.bind("<Key>",handel_keypress)

def handle_click(event):
    print("\nthe button was clicked!")

button= tk.Button(text="click me!")
button.pack()

button.bind("<Button-1>",handle_click)

root.mainloop()