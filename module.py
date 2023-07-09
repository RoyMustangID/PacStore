from datetime import date
import random
import string
from tabulate import tabulate


class Buyer:
    """
    For creating object with a class named Buyer
    with customer name as an input
    """
    def __init__(self, customer_name):
        """Object initialization, customer name as input, only alphabet character is permitted"""
        self.subtotal_list = []                  # Initialize subtotal list, will be summed in calculate_subtotal method
        self.name = customer_name                # Always remember your customer name ;)
        self.transaction_date = date.today()     # Will be used to generate transaction id
        self.shopping_cart = {}                  # Initialize the shopping cart dictionary, all items will be here
        self.transaction_id = self.transaction_date.strftime("%m%d%y") + random.choice(string.ascii_letters) + \
                              random.choice(string.ascii_letters)   # Generate transaction ID
        self.subtotal = 0                        # Initialize subtotal (will be the sum of subtotal_list)
        print(f"Welcome {self.name}")            # A heartwarming welcome is needed
        print(f"Your transaction ID is {self.transaction_id}")

    def calculate_subtotal(self):
        """Called every time add_item , edit_quantity , and edit_price is called. No input"""
        self.subtotal_list.clear()                              # Ensure the subtotal list is clear before appending it
        for key, value in self.shopping_cart.items():           # Loop to fill the subtotal list
            self.subtotal_list.append(self.shopping_cart[key][2])
        self.subtotal = sum(self.subtotal_list)                 # Calculate subtotal from subtotal list

    def add_item(self, item_name, qty, price):
        """Add item to shopping cart with input: the name of the item, the quantity, and price per piece"""
        self.shopping_cart.update({item_name: [qty, price, price * qty]})  # Add new item to shopping cart
        self.calculate_subtotal()                                          # Update the subtotal
        print(f"{item_name} successfully added to the cart")

    def edit_name(self, old_name, new_name):
        """Edit name in shopping cart with input: the name of the item and the new name for the item"""
        self.shopping_cart.update({new_name: self.shopping_cart.get(old_name)})  # Add new key-value to the dictionary
        self.shopping_cart.pop(old_name)                                         # Remove the old key-value
        print(f"Name has been changed to {new_name}")

    def edit_quantity(self, item_name, qty):
        """Edit quantity in shopping cart with input: the name of the item and the new quantity for the item"""
        self.shopping_cart[item_name][0] = qty                                     # Assign new quantity to the item
        self.shopping_cart[item_name][2] = qty * self.shopping_cart[item_name][1]  # Calculate new subtotal for the item
        self.calculate_subtotal()                                                  # Update the subtotal
        print(f"{item_name} quantity has been updated to {qty}")

    def edit_price(self, item_name, price):
        """Edit price per piece in shopping cart with input: the name of the item and the new price for the item"""
        self.shopping_cart[item_name][1] = price                                     # Assign new price to the item
        self.shopping_cart[item_name][2] = price * self.shopping_cart[item_name][0]  # Calculate item's new subtotal
        self.calculate_subtotal()                                                    # Update the subtotal
        print(f"{item_name} price has been updated to {price}")

    def delete_item(self, item_name):
        """Delete existing item in shopping cart with input: item name"""
        self.shopping_cart.pop(item_name)                           # Remove the item from the shopping cart dictionary
        self.calculate_subtotal()
        print(f"{item_name} has been removed from the cart")

    def empty_cart(self):
        """Remove all items in the shopping cart. No input"""
        self.shopping_cart.clear()                                  # Remove all item from the shopping cart
        print(f"All items have been removed from the cart")
        self.calculate_subtotal()

    def show_cart(self):
        """Show items in cart and the subtotal, no input needed"""
        table_header = ("Item", "Quantity", "Price", "Total")   # Header for the table
        print(f"Transaction ID = {self.transaction_id}")        # Show transaction ID
        print(tabulate([[k, ] + v for k, v in self.shopping_cart.items()], headers=table_header))  # Print the table
        print(f"Subtotal = {self.subtotal}")                    # Show subtotal of the transaction

    def total_price(self):
        """Check for discount and applied it to the subtotal. No input"""
        self.show_cart()
        if 200_000 < self.subtotal <= 300_000:              # Check for the eligibility
            self.total = self.subtotal * 0.95               # Apply the discount to calculate total
            self.discount = "5%"
            print(f"Discount applied = {self.discount}")    # Print the discount
        elif 300_000 < self.subtotal <= 500_000:
            self.total = self.subtotal * 0.92
            self.discount = "8%"
            print(f"Discount applied = {self.discount}")
        elif self.subtotal > 500_000:
            self.total = self.subtotal * 0.9
            self.discount = "8%"
            print(f"Discount applied = {self.discount}")
        else:                                               # If no discount requirement is met
            self.total = self.subtotal                      # No discount is applied to calculate total bill
            print("Not eligible for any discount")
        print(f"Your total bill is {self.total}")           # Print the total bill


class Wipe(object):
    """Optional class to help cleaning the interpreter console"""
    def __repr__(self):
        return '\n'*20
