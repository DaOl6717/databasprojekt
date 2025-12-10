# --------- TASK 7 ---------
# 
# Create a Python program which connects to the database, asks the user for a department ID (i.e., the
# value of the primary key) and lists all its products (outputting the ID, the title and the retail price after the
# discount) if the given department is a leaf department, otherwise lists all its child departments (outputting
# the ID and the title).
# Create another program which asks for a product ID, shows the current discount and allows the user to
# change it.
# (You can use another programming language as well, but remember that the assistants might not be able
# to help you if you have problems related to the programming language or a MySQL connector.)
# Please also submit your programming code as separate files (i.e. your “...py” or “...java” files) together
# with instructions how to run them. Please include your code and instructions within your final report as
# well.

from database.schemas.Department import Department
from database.schemas.Keyword import Keyword
from database.schemas.OrderProduct import OrderProduct
from database.schemas.Orders import Orders
from database.schemas.Product import Product
from database.schemas.Review import Review
from database.schemas.Users import Users
from database.Database import Database

def list_price(product):
    pass

def list_menu_options():
    return "[1] List department products/subdepartments", "[2] View and edit product discount"

def prompt_id(prompt, validation_func, convert_func):
    input_id = None
    while not validation_func(input_id := input(prompt)):
        print("Please select a valid ID!")
    
    return convert_func(input_id)

def promt_action():
    print(list_menu_options())
    choice = input("What do you want to do?")
    
    match choice:
        case "1":
            # List department products or subdepartments
            department_id = prompt_department_id()
            show_department(department_id)
        case "2":
            # View and edit product discount
            pass
        case _:
            print(f"The only valid options is 1 or 2, you chose {choice}, you pleb.")

def prompt_department_id():
    return prompt_id("Input the department ID: ", str.isnumeric, int)

def prompt_product_id():
    return prompt_id("Please select a product ID:", str.isnumeric, int)

def show_department(department_id):
    dep: Department = Department(db)
    
    child_departments = dep.list_child_departments(department_id)
    print(child_departments)
    
    #if (child)
    
    #if (child)
    
    #if (child)

def list_child_departments(child_departments):
    pass

def list_department_products(department_id):
    pass

def main(db: Database):
    program_running = True
    
    print("""
╔═══╗╔╗  ╔╗ ╔═══╗    ╔╗           
║╔═╗║║║ ╔╝╚╗║╔═╗║    ║║           
║║ ║║║║ ╚╗╔╝║║ ║║╔═╗ ║║ ╔╗╔═╗ ╔══╗
║╚═╝║║║  ║║ ║║ ║║║╔╗╗║║ ╠╣║╔╗╗║╔╗║
║╔═╗║║╚╗ ║╚╗║╚═╝║║║║║║╚╗║║║║║║║║═╣
╚╝ ╚╝╚═╝ ╚═╝╚═══╝╚╝╚╝╚═╝╚╝╚╝╚╝╚══╝

Den enda platsen där du kan beställa krigsbrott till ett bra pris, pengarna tillbaka garanti om krigsbrottet inte når dina standarder inom 30 dagar!                       
""")
    while (program_running):
        promt_action()

if __name__ == "__main__":
    db = Database()
    db.connect()
    main(db)