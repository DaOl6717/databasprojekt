# Instructions for task 7

These are the instructions to run task 7. 
NOTE: You should only run one file. The two subtasks of task 7 have been combined into one python program.

## Usage

### Running the program
To run the program, run "python3 .\task7.py" in the terminal.
You will be presented with two options. After every input, press enter.

### Using the program
For the first subtask, choose option 1 (press 1 + enter). Now enter a valid department ID. If an ID is chosen that does not match a department ID in the database, an error message will show and you will be promted to enter a valid ID. If a valid ID is chosen, there is two outcomes. Either a department containing subdepartments have been chosen, in that case, all of that department's the subdepartments will be displayed: (ID, Name). If a leaf department is chosen, all the department's products will be displayed: (ID, Name, Retail Price). The user will now be returned to the start page.

For the second subtask, choose option 2. Now select a product ID, if invalid, the user will be prompted again. The product will  be shown. The user will now be asked if they would like to edit the product discount. If "No", the program will return to the start page. If "Yes", the user will be prompted to enter a value between 0 and 100, and the discount procentage will be changed. The user will now be returned to the start page.

## Example run

TODO