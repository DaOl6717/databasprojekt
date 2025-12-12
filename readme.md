# Instructions for task 7

These are the instructions to run task 7. 
NOTE: You should only run one file. The two subtasks of task 7 have been combined into one python program.

## Usage

### Running the program
To run the program, run "python3 .\task7.py" in the terminal.
You will be presented with two options. After every input, press enter.

### Using the program
For the first subtask, choose option 1 (press 1 + enter). Now enter a valid department ID. If an ID is chosen that does not match a department ID in the database, an error message will show and you will be prompted to enter a valid ID. If a valid ID is chosen, there is two outcomes. Either a department containing subdepartments have been chosen, in that case, all of that department's the subdepartments will be displayed: (ID, Name). If a leaf department is chosen, all the department's products will be displayed: (ID, Name, Retail Price). The user will thereafter be returned to the start page.

For the second subtask, choose option 2. Now select a product ID, if invalid, the user will be prompted again. The product will  be shown. The user will now be asked if they would like to edit the product discount. If "No", the program will return to the start page. If "Yes", the user will be prompted to enter a value between 0 and 100, and the discount percentage will be changed. The user will now be returned to the start page.

## Example run

```
python .\task7.py

╔═══╗╔╗  ╔╗ ╔═══╗    ╔╗
║╔═╗║║║ ╔╝╚╗║╔═╗║    ║║
║║ ║║║║ ╚╗╔╝║║ ║║╔═╗ ║║ ╔╗╔═╗ ╔══╗
║╚═╝║║║  ║║ ║║ ║║║╔╗╗║║ ╠╣║╔╗╗║╔╗║
║╔═╗║║╚╗ ║╚╗║╚═╝║║║║║║╚╗║║║║║║║║═╣
╚╝ ╚╝╚═╝ ╚═╝╚═══╝╚╝╚╝╚═╝╚╝╚╝╚╝╚══╝

[1] List department products/subdepartments
[2] View and edit product discount

What do you want to do?: 1
Input the department ID: 10

Department with ID '10' does not exist!

[1] List department products/subdepartments
[2] View and edit product discount

What do you want to do?: 1
Input the department ID: 9

ID: 6 Name: Latte Retail Price: 82.32

[1] List department products/subdepartments
[2] View and edit product discount

What do you want to do?: 1
Input the department ID: 2

ID: 4 Name: I am 0.0
ID: 5 Name: I am 0.1
ID: 6 Name: I am 0.2

[1] List department products/subdepartments
[2] View and edit product discount

What do you want to do?: 2
Please select a product ID: 56

Product with ID '56' does not exist!

[1] List department products/subdepartments
[2] View and edit product discount

What do you want to do?: 2
Please select a product ID: 2
Name: Green Tea Product description: Organic green tea leaves Stock Quantity: 11 Price: 122.1 Discount: 0.0%

Would you like to change the discount for this product? (1 for yes, 2 for no)1
Select a new discount percentage:50
Updated discount to 50%
[1] List department products/subdepartments
[2] View and edit product discount

What do you want to do?: 2
Please select a product ID: 2
Name: Green Tea Product description: Organic green tea leaves Stock Quantity: 11 Price: 61.05 Discount: 50.0%

Would you like to change the discount for this product? (1 for yes, 2 for no)2
[1] List department products/subdepartments
[2] View and edit product discount

What do you want to do?: 3
The only valid options is 1 or 2, you chose a non-valid option (3).
[1] List department products/subdepartments
[2] View and edit product discount
```
