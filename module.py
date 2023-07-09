from datetime import date
import random
import string
from tabulate import tabulate


class Buyer:

    def __init__(self, customer_name):
        self.subtotal_list = []
        self.name = customer_name
        self.transaction_date = date.today()
        self.shopping_cart = {}
        self.transaction_id = self.transaction_date.strftime("%m%d%y") + random.choice(string.ascii_letters) + \
                              random.choice(string.ascii_letters)
        self.subtotal = 0
        print(f"Welcome {self.name}")
        print(f"Your transaction ID is {self.transaction_id}")

    def calculate_subtotal(self):
        self.subtotal_list.clear()
        for key, value in self.shopping_cart.items():
            self.subtotal_list.append(self.shopping_cart[key][2])
        self.subtotal = sum(self.subtotal_list)

    def add_item(self, item_name, qty, price):

        if item_name in self.shopping_cart.keys():
            print("Item with the same name is already exist")
        else:
            self.shopping_cart.update({item_name: [qty, price, price * qty]})
            self.calculate_subtotal()
            print(f"{item_name} successfully added to the cart")

    def edit_name(self, old_name, new_name):
        self.shopping_cart.update({new_name: self.shopping_cart.get(old_name)})
        self.shopping_cart.pop(old_name)
        print(f"Name has been changed to {new_name}")

    def edit_quantity(self, item_name, qty):
        try:
            self.shopping_cart[item_name][0] = qty
            self.shopping_cart[item_name][2] = qty * self.shopping_cart[item_name][1]
            self.calculate_subtotal()
            print(f"{item_name} quantity has been updated to {qty}")
        except Exception as e:
            print(e)

    def edit_price(self, item_name, price):
        try:
            self.shopping_cart[item_name][1] = price
            self.shopping_cart[item_name][2] = price * self.shopping_cart[item_name][0]
            self.calculate_subtotal()
            print(f"{item_name} price has been updated to {price}")
        except Exception as e:
            print(e)

    def delete_item(self, item_name):
        self.shopping_cart.pop(item_name)
        print(f"{item_name} has been removed from the cart")

    def empty_cart(self):
        self.shopping_cart.clear()
        print(self.shopping_cart)
        print(f"All items have been removed from the cart")
        self.calculate_subtotal()

    def show_cart(self):
        table_header = ("Item", "Quantity", "Price", "Total")
        print(f"Transaction ID = {self.transaction_id}")
        print(tabulate([[k, ] + v for k, v in self.shopping_cart.items()], headers=table_header))
        print(f"Subtotal = {self.subtotal}")

    def total_price(self):
        self.show_cart()
        if 200_000 < self.subtotal <= 300_000:
            self.total = self.subtotal * 0.95
            self.discount = "5%"
            print(f"Discount applied = {self.discount}")
        elif 300_000 < self.subtotal <= 500_000:
            self.total = self.subtotal * 0.92
            self.discount = "8%"
            print(f"Discount applied = {self.discount}")
        elif self.subtotal > 500_000:
            self.total = self.subtotal * 0.9
            self.discount = "8%"
            print(f"Discount applied = {self.discount}")
        else:
            self.total = self.subtotal
            print("Not eligible for any discount")
        print(f"Your total bill is {self.total}")


class Wipe(object):
    def __repr__(self):
        return '\n'*20
