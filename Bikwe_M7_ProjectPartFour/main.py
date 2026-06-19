import tkinter as tk
from tkinter import messagebox


# Shopping cart list
cart = []


# Add item to cart
def add_item():
    item = item_entry.get()
    quantity = quantity_entry.get()
    category = category_entry.get()

    if item == "" or quantity == "" or category == "":
        messagebox.showerror("Error", "Please fill out all fields.")
        return

    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a number.")
        return

    cart.append(f"{item} | Quantity: {quantity} | Category: {category}")
    display_cart()
    clear_inputs()


# Display items in cart
def display_cart():
    cart_list.delete(0, tk.END)

    for item in cart:
        cart_list.insert(tk.END, item)

    total_label.config(text=f"Total Items: {len(cart)}")


# Clear cart
def clear_cart():
    cart.clear()
    cart_list.delete(0, tk.END)
    total_label.config(text="Total Items: 0")


# Clear entry boxes
def clear_inputs():
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)


# New order
def new_order():
    clear_cart()
    messagebox.showinfo("New Order", "A new order has started.")


# Exit application
def exit_app():
    window.destroy()


# Main window
window = tk.Tk()
window.title("Nosh & Nibbles Grocery Cart")
window.geometry("500x500")


# Menu
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="New Order", command=new_order)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)


# Labels and entries
tk.Label(window, text="Item Name").pack()
item_entry = tk.Entry(window)
item_entry.pack()

tk.Label(window, text="Quantity").pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

tk.Label(window, text="Category").pack()
category_entry = tk.Entry(window)
category_entry.pack()


# Buttons
tk.Button(window, text="Add Item", command=add_item).pack(pady=5)

tk.Button(window, text="Clear Cart", command=clear_cart).pack(pady=5)


# Cart display
tk.Label(window, text="Shopping Cart").pack()

cart_list = tk.Listbox(window, width=50, height=10)
cart_list.pack()


# Total items
total_label = tk.Label(window, text="Total Items: 0")
total_label.pack(pady=10)


# Run application
window.mainloop()