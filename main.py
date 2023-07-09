"""
This is a cashier program and made so the user does not have to know much about coding to run it
To run the program, the user only needs to run this file as a whole
After the program is running, the user needs to enter their name, and they will be brought
to the main menu.
User can choose what action they want to do and can type 'help' for a list of action available
"""

from module import Buyer        # Import the main Class to run cashier program
from module import Wipe         # Import an optional class to clear interpreter console for cleaner UI

wipe = Wipe()                                                            # Will be used to clear the interpreter console

print("Welcome to PacStore Shop!")                                         # Welcoming message :D
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
            item_name = input("What item do you want to change? ")          # Input key for cart dictionary to edit

            if item_name.lower() == "back":                                 # Back to Action Choice
                break

            elif len(Buyer1.shopping_cart) == 0:                            # Check whether cart is empty
                print("The cart is empty")                                  # If it's empty, nothing can be edited
                break

            elif not item_name.lower() in Buyer1.shopping_cart.keys():      # Check whether item with that name exist
                print("No such item exists")
                print("Please try to input another item or type 'back' to cancel the action")

            else:
                while True:
                    chosen_edit = input("Do you want to change the name, quantity, or price? ")  # Choose what to edit
                    if chosen_edit == "back":                                       # Back to Action Choice
                        break

                    elif chosen_edit.lower() == "name":                             # Edit name action is chosen
                        new_name = input(f"What new name do you want for {item_name.lower()}? ")
                        if new_name.lower() in Buyer1.shopping_cart.keys():         # Check if there are already other
                            print(f"{new_name} already exist in the cart")          # item with the name
                        else:
                            Buyer1.edit_name(item_name.lower(), new_name.lower())   # Call edit_name method
                            break

                    elif chosen_edit == "quantity":                                 # Edit quantity action is chosen
                        new_qty = input("Insert new quantity ")
                        try:
                            Buyer1.edit_quantity(item_name.lower(), int(new_qty))   # Call edit_quantity method
                        except ValueError:
                            print("Quantity should be inputted in whole number")    # Exception if qty is not int
                        break

                    elif chosen_edit == "price":                                    # Edit price action is chosen
                        new_price = input("Insert new price ")
                        try:
                            Buyer1.edit_price(item_name.lower(), int(new_price))    # Call edit_price method
                        except ValueError:
                            print("Price should be inputted in whole number")       # Exception if price is not int
                        break

                    else:
                        print("That option is not available")                       # If the user type outside of name,
                        print("Please choose between name, quantity, and price \n\
              or type 'back' to cancel the action")                                 # quantity or price

                    break
            break

    elif chosen_action.lower() == "delete":                                 # Delete item action is chosen
        print(wipe)                                                         # Clear interpreter console
        while True:
            item_name = input("What item do you want to delete? ")          # User input what item to delete
            if item_name.lower() == 'back':                                 # Back to Action Choice
                break
            elif item_name.lower() not in Buyer1.shopping_cart.keys():      # Check whether item with that name exist
                print("No item with that name exists")
                print("Please try to input another item or type 'back' to cancel the action")
            else:
                Buyer1.delete_item(item_name.lower())                       # Call delete_item method
                break

    elif chosen_action.lower() == "empty":                                  # Empty cart action is chosen
        print(wipe)                                                         # Clear interpreter console
        print("Do you really want to empty your shopping cart?")
        clear_cart = input("Type 'yes' to confirm ")                         # Confirmation
        if clear_cart.lower() == "yes":
            Buyer1.empty_cart()                                             # Call empty_cart method
        else:
            print("Action is cancelled")                                    # Cancel empty cart action

    elif chosen_action.lower() == "show":                                   # Show cart action is chosen
        print(wipe)                                                         # Clear interpreter console
        Buyer1.show_cart()                                                  # Call show_cart method

    elif chosen_action.lower() == "total":
        print(wipe)                                                         # Clear interpreter console

        if len(Buyer1.shopping_cart) == 0:                                  # Check if the cart is empty
            print("The cart is empty")                                      # Total can't be calculated if cart is empty

        else:
            Buyer1.total_price()                                            # Call total_price method
            print("Advance to payment?")
            payment = input("Type 'yes' to confirm ")                       # Confirmation to pay (end program)
            if payment.lower() == "yes":                                    # Confirmed to end the program
                print(f"Thank you, {Buyer1.name} \n\
        Please use your Transaction ID {Buyer1.transaction_id} for payment \n\
        We hope for your return")
                break
            else:                                                           # Program not ended
                print("You did not confirm the payment, please continue your shopping")  # Continue shopping

    elif chosen_action.lower() == "cancel":                                 # Cancel transaction action is chosen
        print(wipe)                                                         # Clear interpreter console
        print("Do you really want to cancel the transaction?")
        leave_shop = input("Type 'yes' to confirm ")                        # Confirmation of transaction cancellation
        if leave_shop.lower() == "yes":                                     # Confirmation to cancel the transaction
            print("Your transaction is successfully cancelled")             # Confirmed to end the program
            break
        else:                                                               # Program not ended
            print("You did not confirm the cancellation, please continue your shopping")  # Continue shopping

    else:
        print("That Action is not available")                               # If user input other than available actions
        print("You can type 'help' to see what actions are available.")