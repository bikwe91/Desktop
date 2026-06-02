# Initialize the inventory dictionary

grocery_inventory = {

    'Apple': ('Fruit', 50, 0.50),

    'Banana': ('Fruit', 100, 0.30),

    'Orange': ('Fruit', 60, 0.75),

    'Grapes': ('Fruit', 40, 2.50),

    'Bread': ('Bakery', 30, 2.00),

    # Add more items as needed

}

 

def add_item(inventory, item_name, category, quantity, price):

    if item_name in inventory:

        return f"{item_name} already exists in the inventory."

    else:

        inventory[item_name] = (category, quantity, price)

        return f"{item_name} added to the inventory."

 

def update_quantity(inventory, item_name, quantity):

    if item_name in inventory:

        category, current_quantity, price = inventory[item_name]

        inventory[item_name] = (category, current_quantity + quantity, price)

        return f"Updated {item_name} quantity to {inventory[item_name][1]}."

    else:

        return f"{item_name} not found in the inventory."

 

def calculate_total_value(inventory):

    total_value = 0

    for item, details in inventory.items():

        total_value += details[1] * details[2]

    return total_value