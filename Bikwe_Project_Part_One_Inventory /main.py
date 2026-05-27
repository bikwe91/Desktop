# Fabrice Bikwe
# IT211 - Project Part One: Inventory

inventory = {
    "Apple": {"category": "Fruit", "quantity": 50, "price": "$0.50"},
    "Bacon": {"category": "Meat", "quantity": 25, "price": "$4.50"},
    "Banana": {"category": "Fruit", "quantity": 100, "price": "$0.30"},
    "Bread": {"category": "Bakery", "quantity": 30, "price": "$2.00"},
    "Carrots": {"category": "Produce", "quantity": 60, "price": "$1.00 per lb"},
    "Chicken breast": {"category": "Meat", "quantity": 50, "price": "$5.00 per lb"},
    "Coffee": {"category": "Beverage", "quantity": 20, "price": "$8.00 per lb"},
    "Eggs": {"category": "Dairy", "quantity": 40, "price": "$2.50 per dozen"},
    "Ground Beef": {"category": "Meat", "quantity": 40, "price": "$4.00 per lb"},
    "Lettuce": {"category": "Produce", "quantity": 40, "price": "$1.50"},
    "Milk": {"category": "Dairy", "quantity": 25, "price": "$3.00 per gallon"},
    "Orange Juice": {"category": "Beverage", "quantity": 30, "price": "$4.00 per gallon"},
    "Peanut Butter": {"category": "Pantry", "quantity": 25, "price": "$3.00"},
    "Rice": {"category": "Pantry", "quantity": 100, "price": "$1.20 per lb"}
}


def display_inventory():
    print("\n--- Current Inventory ---")
    for item, details in inventory.items():
        print(f"{item}:")
        print(f"  Category: {details['category']}")
        print(f"  Quantity: {details['quantity']}")
        print(f"  Price: {details['price']}")


def search_item():
    item_name = input("\nEnter the item name to search: ").title()

    if item_name in inventory:
        print("\nItem found:")
        print(f"Item: {item_name}")
        print(f"Category: {inventory[item_name]['category']}")
        print(f"Quantity: {inventory[item_name]['quantity']}")
        print(f"Price: {inventory[item_name]['price']}")
    else:
        print("Item not found in the inventory.")


def update_item():
    item_name = input("\nEnter the item name to update: ").title()

    if item_name in inventory:
        print("\nWhat would you like to update?")
        print("1. Category")
        print("2. Quantity")
        print("3. Price")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_category = input("Enter new category: ")
            inventory[item_name]["category"] = new_category
            print("Category updated successfully.")

        elif choice == "2":
            try:
                new_quantity = int(input("Enter new quantity: "))
                inventory[item_name]["quantity"] = new_quantity
                print("Quantity updated successfully.")
            except ValueError:
                print("Invalid input. Quantity must be a number.")

        elif choice == "3":
            new_price = input("Enter new price: ")
            inventory[item_name]["price"] = new_price
            print("Price updated successfully.")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    else:
        print("Item not found in the inventory.")


def add_item():
    item_name = input("\nEnter new item name: ").title()

    if item_name in inventory:
        print("This item already exists in the inventory.")
    else:
        category = input("Enter category: ")

        try:
            quantity = int(input("Enter quantity: "))
            price = input("Enter price: ")

            inventory[item_name] = {
                "category": category,
                "quantity": quantity,
                "price": price
            }

            print("Item added successfully.")

        except ValueError:
            print("Invalid input. Quantity must be a number.")


def main_menu():
    while True:
        print("\n--- Nash & Nibbles Inventory System ---")
        print("1. Display Inventory")
        print("2. Search Item")
        print("3. Update Item")
        print("4. Add Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_inventory()
        elif choice == "2":
            search_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            add_item()
        elif choice == "5":
            print("Thank you for using the inventory system.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main_menu()