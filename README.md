# PacStore Self-Cashier
This program is made so the user does not have to know much about coding to run it.<br />
To run the program, the user only needs to run main.py file as a whole.<br />
After the program is running, the user needs to enter their name, and they will be brought
to the main menu.<br />
User can choose what action they want to do and can type 'help' for a list of action available.<br />
## Background
A simple python self-cashier program for a supermarket

## Library Requirements
tabulate==0.9.0

## Project Requirements
### 1. Transaction ID
Generating transaction ID for the customer to start shopping
### 2. Add item
Add new items to the customer cart. It should have at least three properties: item name, quantity, and price per piece
### 3. Check Order (Show Cart)
Show the list of all items in the cart.
### 4. Edit item
Change existing item inside the cart:
 - Edit Name
 - Edit Quantity
 - Edit Price per piece
### 5. Delete item
Delete an existing item iside the cart
### 6. Clear / Empty the cart
Delete all item inside the cart
### 7. Sub Total Price (before discount)
Calculate the total price of all item inside the cart
### 8. Calculate Discount
Add discount with criteria:
 - Sub total more than 200.000 => 5% discount
 - Sub total more than 300.000 => 8% discount
 - Sub total more than 500.000 => 10% discount
### 9. Total Price
Calculate the total price after discount is applied


## Development and Solution Sketch
![image](https://github.com/RoyMustangID/PacStore/assets/99116820/0eff64cd-c348-43b9-a4cf-5d360eea7064)

## Flowchart
![SIMPLE REQUIREMENT AND CODE PLANNING](https://github.com/RoyMustangID/PacStore/assets/99116820/11b87eb5-2fb6-480a-8c69-b84625a27039)

## Test Case

### Test Case 1
#### Given Case
Customer wants to add this item
- Ayam Goreng, Qty = 2 , Price = 20000
- Pasta Gigi, Qty = 3 , Price = 15000
#### Testing it on the script
* Adding the item with add_item method
  ![image](https://github.com/RoyMustangID/PacStore/assets/99116820/5a76b894-f893-46b4-bb24-fd120c0cf916)
  ![image](https://github.com/RoyMustangID/PacStore/assets/99116820/70017e0b-d509-4f24-b388-6cc84bc7ddd9)
* Show the item using show_cart method
  ![image](https://github.com/RoyMustangID/PacStore/assets/99116820/470ae983-917a-4518-9ac4-59822232f583)

### Test Case 2
#### Given Case
Customer wants to delete Pasta Gigi from the shopping cart

#### Testing it on the script
* Delete item with delete_item method
![image](https://github.com/RoyMustangID/PacStore/assets/99116820/69c4cc66-366e-450c-8fcf-d97a64b38652)
* Show the item using show_cart method
![image](https://github.com/RoyMustangID/PacStore/assets/99116820/f718a2f0-02a8-41de-8987-12e1f319bdc5)

### Test Case 3
#### Given Case
Customer wants to reset the transaction

#### Testing it on the script
* Reset transaction with empty_cart method
![image](https://github.com/RoyMustangID/PacStore/assets/99116820/6d4d4516-e0c0-41ac-818e-4b22ab8b0cc7)
* Show the item using show_cart method
![image](https://github.com/RoyMustangID/PacStore/assets/99116820/3e94b180-73af-4c66-9067-319925c968b2)

### Test Case 4
#### Given Case
Customer wants to calculate the total bill and show all item

#### Testing it on the script
* Show all item and calculate total bill using total_price method
  ![image](https://github.com/RoyMustangID/PacStore/assets/99116820/bcf6fe66-a8c9-4711-a3de-a1dbd178959d)

## Conclusion
The program meets all the requirement for a self-cashier application and pass all test cases

## Credit
This program is created by Paripurna Bawononoputro for Pacmann Academy project




