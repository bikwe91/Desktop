# Item Class
class Item:
    def __init__(self, name, quantity, price, category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def update_quantity(self, quantity):
        self.quantity = quantity

    def update_price(self, price):
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def display(self):
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.price:.2f}")
        print(f"Category: {self.category}")
        print(f"Total Value: ${self.total_value():.2f}")
        print("-" * 30)


# Inventory Class
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def update_item(self, item_name, quantity=None, price=None):
        for item in self.items:
            if item.name == item_name:
                if quantity is not None:
                    item.update_quantity(quantity)
                if price is not None:
                    item.update_price(price)

    def display_inventory(self):
        print("\nCURRENT INVENTORY")
        print("=" * 30)
        for item in self.items:
            item.display()

    def search_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.display()
                return
        print("Item not found.")


# Main Program
inventory = Inventory()

# Add items
inventory.add_item(Item("Apples", 50, 0.99, "Produce"))
inventory.add_item(Item("Milk", 20, 3.49, "Dairy"))
inventory.add_item(Item("Bread", 15, 2.99, "Bakery"))

# Display inventory
inventory.display_inventory()

# Update an item
inventory.update_item("Milk", quantity=25, price=3.79)

print("\nUPDATED ITEM")
print("=" * 30)
inventory.search_item("Milk")

# Remove an item
inventory.remove_item("Bread")

print("\nINVENTORY AFTER REMOVING BREAD")
print("=" * 30)
inventory.display_inventory()