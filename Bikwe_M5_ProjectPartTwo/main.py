from inventory import grocery_inventory, add_item, update_quantity, calculate_total_value

 

# List of item names

item_names = list(grocery_inventory.keys())

 

# Display the inventory

for item in item_names:

    details = grocery_inventory[item]

    print(f"{item}: Category: {details[0]}, Quantity: {details[1]}, Price: ${details[2]:.2f}")

 

# Add a new item to the inventory

new_item_name = 'Milk'

new_item_details = ('Dairy', 25, 3.00)

if new_item_name not in grocery_inventory:

    grocery_inventory[new_item_name] = new_item_details

    item_names.append(new_item_name)

    print(f"{new_item_name} added to the inventory.")

else:

    print(f"{new_item_name} already exists in the inventory.")

 

# Update the quantity of an existing item

update_item_name = 'Apple'

if update_item_name in grocery_inventory:

    category, current_quantity, price = grocery_inventory[update_item_name]

    new_quantity = current_quantity + 20  # Students can change the quantity to update

    grocery_inventory[update_item_name] = (category, new_quantity, price)

    print(f"Updated {update_item_name} quantity to {new_quantity}.")

else:

    print(f"{update_item_name} not found in the inventory.")

 

# Calculate the total value of the inventory

total_value = calculate_total_value(grocery_inventory)

print(f"Total value of inventory: ${total_value:.2f}")