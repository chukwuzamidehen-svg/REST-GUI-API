import tkinter as tk
from tkinter import messagebox
import re
import requests

API_URL = "http://127.0.0.1:5000/purchase"

root = tk.Tk()
root.title("Purchase Entry System")
root.geometry("450x500")

# Form heading
tk.Label(root, text="Purchase Entry Form", font=("Arial", 18, "bold")).pack(pady=15)


# Helper function for text fields
def create_field(label):
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root, width=40)
    entry.pack(pady=5)
    return entry


product_id = create_field("Product ID")
description = create_field("Description")
customer_name = create_field("Customer Name")
customer_email = create_field("Customer Email")
price = create_field("Price ($)")

# Checkbox for online/in-store purchase
is_online = tk.BooleanVar(value=False)

tk.Checkbutton(
    root, text="Online Purchase (unchecked = In-Store)", variable=is_online
).pack(pady=10)


def submit_purchase():
    # Collect form values
    email = customer_email.get().strip()
    price_text = price.get().strip()

    # Validate required fields
    if not all(
        [
            product_id.get().strip(),
            description.get().strip(),
            customer_name.get().strip(),
            email,
            price_text,
        ]
    ):
        messagebox.showerror("Validation Error", "Please complete all fields.")
        return

    # Validate email format locally
    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.fullmatch(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    # Validate price locally
    try:
        purchase_price = float(price_text)
    except ValueError:
        messagebox.showerror("Invalid Price", "Price must be a number.")
        return

    if not 0 <= purchase_price <= 1000:
        messagebox.showerror("Invalid Price", "Price must be between $0 and $1,000.")
        return

    # Package purchase information as JSON
    payload = {
        "product_id": product_id.get().strip(),
        "description": description.get().strip(),
        "customer_name": customer_name.get().strip(),
        "customer_email": email,
        "price": purchase_price,
        "is_online": is_online.get(),
    }

    # Send JSON to Flask API
    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        result = response.json()

        if response.status_code == 201:
            messagebox.showinfo("Success", result["message"])
        else:
            messagebox.showerror("API Error", result.get("error", "Unknown error"))

    except requests.RequestException:
        messagebox.showerror("Connection Error", "Could not connect to the Flask API.")
    except ValueError:
        messagebox.showerror("Response Error", "The API returned an invalid response.")


# Submit button
tk.Button(
    root,
    text="Submit Purchase",
    command=submit_purchase,
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=8,
).pack(pady=20)

root.mainloop()
