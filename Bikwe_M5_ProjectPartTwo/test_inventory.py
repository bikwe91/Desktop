import unittest
from inventory import grocery_inventory, add_item, update_quantity, calculate_total_value

class TestInventory(unittest.TestCase):

    def test_add_item(self):
        add_item(grocery_inventory, "Tomato", "Vegetable", 10, 2.00)
        self.assertIn("Tomato", grocery_inventory)

    def test_update_quantity(self):
        add_item(grocery_inventory, "Potato", "Vegetable", 5, 1.00)
        update_quantity(grocery_inventory, "Potato", 15)
        self.assertEqual(grocery_inventory["Potato"][1], 20)

    def test_calculate_total_value(self):
        total = calculate_total_value(grocery_inventory)
        self.assertGreater(total, 0)

if __name__ == "__main__":
    unittest.main()