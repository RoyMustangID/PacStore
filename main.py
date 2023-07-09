"""
This is a cashier program and made so the user does not have to know much about coding
To run the program, the user only needs to run this file as a whole
After the program is running, the user needs to enter their name, and they will be brought
to the main menu.
User can choose what action they want to do and can type 'help' for a list of action available
"""

from module import Buyer        # Import the main Class to run cashier program
from module import Wipe         # Import an optional class to clear interpreter console for cleaner UI

wipe = Wipe()                   # Will be used to clear the interpreter console

print("Welcome to PacStore Shop!")                                         # Welcoming message
while True:                                                                # Loop used to ensure the name input is valid
    input_name = input("Customer Name = ")
    customer_name = input_name.upper()
    if not all([letter.isalpha() or letter.isspace() for letter in customer_name]):  # Ensure only alphabet is entered
        print("Error - Only letters are allowed")
    elif len(customer_name) > 10:                                           # To limit name length
        print("Error - Only 10 characters allowed")
    else:
        Buyer1 = Buyer(customer_name)                                       # Create an Object from class Buyer
        break


print("\n You can type 'help' to see what actions are available.")          # A gentle reminder :)
while True:
    chosen_action = input("Action you want to do: ")                        # For receiving action the user want to do

    if chosen_action.lower() == "help":                                     # List of action, called using 'help'
        print("Available actions: \n\
    'add' = Add new item to cart \n\
    'edit' = Edit an existing item in the cart \n\
    'delete' = Delete an existing item in the cart \n\
    'empty' = Remove all items in the cart \n\
    'show' = Show all items in the cart \n\
    'total' = Calculate your bill \n\
    'cancel' = Cancel your order")
        chosen_action = input("Action you want to do: ")                    # User choose action using help

    if chosen_action.lower() == "add":
        print(wipe)                                                         # Clear interpreter console
        while True:
            item_name = input("Item name you want to add = ")
            if item_name.lower() == 'back':                                 # Back to choose action menu
                break
            elif item_name.lower() in Buyer1.shopping_cart.keys():          # Check whether the item name already exists
                print("Item with the same name already exists")
                print("Please try to input another item or type 'back' to cancel the action")
            else:
                item_qty = input("Item quantity = ")
                item_price = input("Item price per piece = ")
                try:
                    Buyer1.add_item(item_name.lower(), int(item_qty), int(item_price))  # Call add_item method
                except ValueError:
                    print("Quantity and Price should be inputted in whole number")  # Exception if qty and price not int
                break

    elif chosen_action.lower() == "edit":
        print(wipe)                                                         # Clear interpreter console
        while True:
            item_name = input("What item do you want to change? ")

            if item_name.lower() == "back":
                break

            elif len(Buyer1.shopping_cart) == 0:
                print("The cart is empty")
                break

            elif not item_name.lower() in Buyer1.shopping_cart.keys():
                print("No such item exists")
                print("Please try to input another item or type 'back' to cancel the action")

            else:
                while True:
                    chosen_edit = input("Do you want to change the name, quantity, or price? ")
                    if chosen_edit == "back":
                        break

                    elif chosen_edit.lower() == "name":
                        new_name = input(f"What new name do you want for {item_name.lower()}? ")
                        if new_name.lower() in Buyer1.shopping_cart.keys():
                            print(f"{new_name} already exist in the cart")
                        else:
                            Buyer1.edit_name(item_name.lower(), new_name.lower())
                            break

                    elif chosen_edit == "quantity":
                        new_qty = input("Insert new quantity ")
                        try:
                            Buyer1.edit_quantity(item_name.lower(), int(new_qty))
                        except ValueError:
                            print("Quantity should be inputted in whole number")
                        break

                    elif chosen_edit == "price":
                        new_price = input("Insert new price ")
                        try:
                            Buyer1.edit_price(item_name.lower(), int(new_price))
                        except ValueError:
                            print("Price should be inputted in whole number")
                        break

                    else:
                        print("That option is not available")
                        print("Please choose between name, quantity, and price \n\
              or type 'back' to cancel the action")

                    break
            break

    elif chosen_action.lower() == "delete":
        print(wipe)                                                         # Clear interpreter console
        while True:
            item_name = input("What item do you want to delete? ")
            if item_name.lower() == 'back':
                break
            elif item_name.lower() not in Buyer1.shopping_cart.keys():      #
                print("No item with that name exists")
                print("Please try to input another item or type 'back' to cancel the action")
            else:
                Buyer1.delete_item(item_name.lower())
                break

    elif chosen_action.lower() == "empty":
        print(wipe)                                                         # Clear interpreter console
        print("Do you really want to empty your shopping cart?")
        clear_cart = input("Type 'yes' to confirm")
        if clear_cart.lower() == "yes":
            Buyer1.empty_cart()
        else:
            print("Action is cancelled")

    elif chosen_action.lower() == "show":
        print(wipe)                                                         # Clear interpreter console
        Buyer1.show_cart()

    elif chosen_action.lower() == "total":
        print(wipe)                                                         # Clear interpreter console

        if len(Buyer1.shopping_cart) == 0:
            print("The cart is empty")

        else:
            Buyer1.total_price()
            print("Advance to payment?")
            payment = input("Type 'yes' to confirm ")
            if payment.lower() == "yes":
                print(f"Thank you, {Buyer1.name} \n\
        Please use your Transaction ID {Buyer1.transaction_id} for payment \n\
        We hope for your return")
                break
            else:
                print("You did not confirm the payment, please continue your shopping")

    elif chosen_action.lower() == "cancel":
        print(wipe)                                                         # Clear interpreter console
        print("Do you really want to cancel the transaction?")
        leave_shop = input("Type 'yes' to confirm ")
        if leave_shop.lower() == "yes":
            print("Your transaction is successfully cancelled")
            break
        else:
            print("You did not confirm the cancellation, please continue your shopping")

    else:
        print("That Action is not available")
