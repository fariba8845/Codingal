import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Reading Planner")
root.geometry("400x300")
root.config(bg="light blue")

tk.Label(root, text="Reading Planner", font=("Arial", 22, "bold"), bg="light blue").pack(pady=40)
tk.Label(root, text="Create a plan for finishing your reading.", bg="light blue").pack(pady=10)

def topwin():
    win = tk.Toplevel(root)
    win.title("Reading Plan")
    win.geometry("400x400")
    win.config(bg="light blue")

    tk.Label(win, text="Total Pages", bg="light blue").pack(pady=5)
    total_entry = tk.Entry(win)
    total_entry.pack()

    tk.Label(win, text="Pages Per Day", bg="light blue").pack(pady=5)
    daily_entry = tk.Entry(win)
    daily_entry.pack()

    tk.Label(win, text="Complete Days", bg="light blue").pack(pady=5)
    days_entry = tk.Entry(win)
    days_entry.pack()

    tk.Label(win, text="Remaining Pages", bg="light blue").pack(pady=5)
    remaining_entry = tk.Entry(win)
    remaining_entry.pack()

    def calculate_plan():
        try:
            total = int(total_entry.get())
            daily = int(daily_entry.get())

            if total <= 0 or daily <= 0:
                raise ValueError

            days = total // daily
            remaining = total % daily

            days_entry.delete(0, tk.END)
            days_entry.insert(0, days)

            remaining_entry.delete(0, tk.END)
            remaining_entry.insert(0, remaining)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter positive whole numbers.")

    tk.Button(win, text="Calculate Plan", command=calculate_plan).pack(pady=25)

tk.Button(root, text="Open Reading Plan", command=topwin).pack(pady=20)

root.mainloop()