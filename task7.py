# --------- TASK 7 ---------
# 
# Gjort:
# Create a Python program which connects to the database, asks the user for a department ID (i.e., the
# value of the primary key)
# and lists all its products (outputting the ID, the title and the retail price after the
# discount)
# if the given department is a leaf department, otherwise lists all its child departments (outputting
# the ID and the title).
# TODO vvvvvvvvv
# Create another program which asks for a product ID, shows the current discount and allows the user to
# change it.
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

def prompt(prompt, retry_prompt, validation_func, convert_func):
    input_id = None
    while not validation_func(input_id := input(prompt)):
        print(retry_prompt)
    
    return convert_func(input_id)

def prompt_id(prompt_a, validation_func, convert_func):
    return prompt(prompt_a, "Please select a valid ID!", validation_func, convert_func)


def prompt_department_id():
    return prompt_id("Input the department ID: ", str.isnumeric, int)

def prompt_product_id():
    return prompt_id("Please select a product ID: ", str.isnumeric, int)

def validate_discount(n):
    return n.isnumeric() and 0 <= int(n) <= 100
    
def prompt_discount():
    return prompt("Select a new discount percentage:", "Please select a valid discount!", validate_discount, int)
    

def list_departments(child_departments):
    print()
    for (dep_id, department_name) in child_departments:
        print(f"ID: {dep_id} Name: {department_name}")
    print()

def list_department_products(db, department_products):
    print()
    for (prod_id, prod_name, discount, vat, price_excl_vat) in department_products:
        price_info = (price_excl_vat, vat, discount)
        current_price = Product.calculate_price(db, price_info)
        print(f"ID: {prod_id} Name: {prod_name} Retail Price: {round(current_price, 2)}")
    print()

def show_product(product):
    print(product) 

def show_department_content(db, department_id):
    dep: Department = Department(db)
    prod: Product = Product(db)
    child_departments = dep.list_child_departments(department_id)
    
    if (len(child_departments) > 0):
        list_departments(child_departments)
        return
    
    department_products = prod.list_products_in_department(department_id)
    
    if (len(department_products) > 0):
        department_products = prod.list_products_in_department(department_id)
        list_department_products(db, department_products)
    else:
        print()
        print(f"Department with ID '{department_id}' does not exist!")   
        print() 
        
def update_discount(db, product_id):
    prod = Product(db)
    new_discount = prompt_discount()/100

    prod.update_discount(product_id, new_discount)
    return int(new_discount*100)

def prompt_action(db):
    print(*list_menu_options(), sep="\n")
    print()
    choice = input("What do you want to do?: ")
    
    match choice:
        case "1":
            # List department products or subdepartments
            department_id = prompt_department_id()
            show_department_content(db, department_id)
        case "2":
            product_id = prompt_product_id()
            # TODO: Kolla att det är ett valid input, annars fråga igen
            # TODO: Hitta produkten
            # TODO: Fråga om man vill ändra produktens discount
            # TODO: Om ja, ändra produktens discount
            discount = update_discount(db, product_id)
            print(f"Updated discount to {discount}%")
            # View and edit product discount
            pass
        case _:
            print(f"The only valid options is 1 or 2, you chose {choice}, you pleb.")
            
def main(db: Database):
    program_running = True
    
    print("""
╔═══╗╔╗  ╔╗ ╔═══╗    ╔╗
║╔═╗║║║ ╔╝╚╗║╔═╗║    ║║
║║ ║║║║ ╚╗╔╝║║ ║║╔═╗ ║║ ╔╗╔═╗ ╔══╗
║╚═╝║║║  ║║ ║║ ║║║╔╗╗║║ ╠╣║╔╗╗║╔╗║
║╔═╗║║╚╗ ║╚╗║╚═╝║║║║║║╚╗║║║║║║║║═╣
╚╝ ╚╝╚═╝ ╚═╝╚═══╝╚╝╚╝╚═╝╚╝╚╝╚╝╚══╝        
""")
    while (program_running):
        prompt_action(db)

if __name__ == "__main__":
    db = Database()
    db.connect()
    main(db)