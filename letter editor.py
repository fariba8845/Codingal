import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Text Editor")
window.geometry("800x500")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

def open_letter():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        text_editor.delete("1.0", tk.END)

        with open(file_path, "r") as file:
            contents = file.read()

        text_editor.insert("1.0", contents)
        window.title(f"Text Editor - {file_path}")

def save_letter():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        contents = text_editor.get("1.0", tk.END)

        with open(file_path, "w") as file:
            file.write(contents)

button_frame = tk.Frame(window)

open_button = tk.Button(
    button_frame,
    text="Open Letter",
    command=open_letter
)

save_button = tk.Button(
    button_frame,
    text="Save Letter As",
    command=save_letter
)

text_editor = tk.Text(window)

open_button.grid(row=0, column=0, padx=5, pady=5)
save_button.grid(row=1, column=0, padx=5, pady=5)

button_frame.grid(row=0, column=0, sticky="ns")
text_editor.grid(row=0, column=1, sticky="nsew")

window.mainloop()