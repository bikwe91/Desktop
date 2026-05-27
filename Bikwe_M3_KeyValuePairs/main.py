# 4.6 Activity - Key-Value Pairs
# Food ordering system for a small cafe

# Create the menu using a dictionary
menu = {
    "Coffee": 2.50,
    "Tea": 2.00,
    "Sandwich": 5.00,
    "Salad": 4.50
}

# Display the menu
print("Cafe Menu:")
for item, price in menu.items():
    print(item + ": $" + str(price))

# Add a new menu item
menu["Muffin"] = 3.00

# Update the price of an existing item
menu["Coffee"] = 2.75

print("\nUpdated Menu:")
for item, price in menu.items():
    print(item + ": $" + str(price))

# Retrieve the price of a specific item
item_to_find = "Sandwich"

if item_to_find in menu:
    print("\nThe price of " + item_to_find + " is $" + str(menu[item_to_find]))
else:
    print("\nItem not found.")

# Remove a menu item
item_to_remove = "Tea"

if item_to_remove in menu:
    del menu[item_to_remove]
    print("\n" + item_to_remove + " was removed from the menu.")
else:
    print("\nItem not found, so it cannot be removed.")

# Final menu
print("\nFinal Menu:")
for item, price in menu.items():
    print(item + ": $" + str(price))