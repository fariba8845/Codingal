import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class StationeryOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Stationery Order Management")
        self.root.geometry("900x600")

        self.stationery = {
            "Pen": 1.50,
            "Pencil": 0.75,
            "Notebook": 4.00,
            "Eraser": 0.50,
            "Ruler": 2.00,
            "Marker": 1.75,
            "Glue": 2.50
        }

        self.exchange_rate = 120
        self.currency = tk.StringVar(value="USD")
        self.quantities = {}

        self.setup_background()

    def setup_background(self):
        self.canvas = tk.Canvas(self.root, width=900, height=600)
        self.canvas.pack(fill="both", expand=True)

        image = Image.open("C:\\Users\\Hp\\Downloads\\background 1.jpeg")
        image = image.resize((900, 600))
        self.background_image = ImageTk.PhotoImage(image)

        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        self.frame = ttk.Frame(self.canvas, padding=20)
        self.canvas.create_window(450, 300, window=self.frame)

        ttk.Label(
            self.frame,
            text="Stationery Order Management",
            font=("Arial", 22, "bold")
        ).grid(row=0, column=0, columnspan=4, pady=15)

        ttk.Label(
            self.frame,
            text="Currency:"
        ).grid(row=1, column=0, padx=10, pady=10)

        currency_box = ttk.Combobox(
            self.frame,
            textvariable=self.currency,
            values=["USD", "BDT"],
            state="readonly",
            width=10
        )
        currency_box.grid(row=1, column=1, pady=10)
        currency_box.bind("<<ComboboxSelected>>", self.update_item_prices)

        ttk.Label(
            self.frame,
            text="Item",
            font=("Arial", 11, "bold")
        ).grid(row=2, column=0, padx=15, pady=8)

        ttk.Label(
            self.frame,
            text="Price",
            font=("Arial", 11, "bold")
        ).grid(row=2, column=1, padx=15, pady=8)

        ttk.Label(
            self.frame,
            text="Quantity",
            font=("Arial", 11, "bold")
        ).grid(row=2, column=2, padx=15, pady=8)

        ttk.Label(
            self.frame,
            text="Total",
            font=("Arial", 11, "bold")
        ).grid(row=2, column=3, padx=15, pady=8)

        self.price_labels = {}
        self.total_labels = {}

        for row, (item, price) in enumerate(self.stationery.items(), start=3):
            ttk.Label(
                self.frame,
                text=item
            ).grid(row=row, column=0, padx=15, pady=5)

            price_label = ttk.Label(self.frame, text="")
            price_label.grid(row=row, column=1, padx=15, pady=5)
            self.price_labels[item] = price_label

            quantity = ttk.Entry(self.frame, width=10)
            quantity.grid(row=row, column=2, padx=15, pady=5)
            self.quantities[item] = quantity

            total_label = ttk.Label(self.frame, text="0.00")
            total_label.grid(row=row, column=3, padx=15, pady=5)
            self.total_labels[item] = total_label

        button_row = len(self.stationery) + 4

        ttk.Button(
            self.frame,
            text="Place Order",
            command=self.place_order
        ).grid(row=button_row, column=0, columnspan=4, pady=15)

        self.update_item_prices()

    def update_item_prices(self, event=None):
        symbol = "$" if self.currency.get() == "USD" else "৳"
        rate = 1 if self.currency.get() == "USD" else self.exchange_rate

        for item, price in self.stationery.items():
            converted_price = price * rate
            self.price_labels[item].config(
                text=f"{symbol}{converted_price:.2f}"
            )

    def place_order(self):
        symbol = "$" if self.currency.get() == "USD" else "৳"
        rate = 1 if self.currency.get() == "USD" else self.exchange_rate

        summary = []
        grand_total = 0

        for item, price in self.stationery.items():
            value = self.quantities[item].get()

            if value == "":
                quantity = 0
            elif value.isdigit():
                quantity = int(value)
            else:
                messagebox.showerror(
                    "Invalid Quantity",
                    f"Please enter a valid quantity for {item}."
                )
                return

            item_total = price * rate * quantity
            grand_total += item_total

            self.total_labels[item].config(
                text=f"{symbol}{item_total:.2f}"
            )

            if quantity > 0:
                summary.append(
                    f"{item}: {quantity} × {symbol}{price * rate:.2f}"
                )

        if not summary:
            messagebox.showwarning(
                "Empty Order",
                "Please enter at least one quantity."
            )
            return

        summary.append("")
        summary.append(
            f"Total: {symbol}{grand_total:.2f}"
        )

        messagebox.showinfo(
            "Order Summary",
            "\n".join(summary)
        )


root = tk.Tk()
app = StationeryOrderManagement(root)
root.mainloop()