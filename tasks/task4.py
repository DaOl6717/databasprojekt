from database.schemas.Department import Department
from database.schemas.Keyword import Keyword
from database.schemas.OrderProduct import OrderProduct
from database.schemas.Orders import Orders
from database.schemas.Product import Product
from database.schemas.Review import Review
from database.schemas.Users import Users

def task4(db):
    department = Department(db)
    keywords = Keyword(db)
    order_product = OrderProduct(db)
    orders = Orders(db)
    product = Product(db)
    review = Review(db)
    users = Users(db)

    ### Home Page ###
    homepage = department.create_department("Home Page", "Welcome text for the home page!")
    
    ### Top-level departments ###
    dep_root1 = department.create_department('Root 1', 'Call a bondulance', homepage)
    dep_root2 = department.create_department('Root 2', 'Call a bondulance', homepage)

    ### Child departments ###
    children = []
    for i in range(6):
        children.append(department.create_department(f"I am {i//3}.{i}", "Call a bondulance", [dep_root1, dep_root2][i//3]))

    ### Products ###
    products = []
    names = ["Coffee", "Green Tea", "Tea", "Espresso", "Black Tea", "Latte", "Herbal Tea", "Cappuccino", "Oolong Tea", "Mocha"]
    descs = ["Freshly brewed coffee", "Organic green tea leaves", "Spill the tea", "Strong italian espresso", "Rich black tea", "Creamy milk latte", "Relaxing herbal blend", "Frothy cappuccino", "Premium oolong tea", "Chocolate flavoured coffee"]

    for i in range(10):
        quantity = 10*i + 1
        vat = i/10 + 0.01
        discount = 2*(i+1)/100
        price_excl_vat = i * 10 + 100
        is_featured = i%2
        parent_department = children[i%6]
        products.append(product.create_product(names[i], descs[i], quantity, vat, discount, price_excl_vat, is_featured, parent_department))

    ### Users ###
    user1 = users.create_user("0405040000", "+000701234567", "mario@yahoo.com", "Filop", "Address 1", False)
    user2 = users.create_user("0407080000", '+000701234568', 'luigi@yahoo.com', 'Davud', 'Address 2', True)
    
    ### Order ###
    order = orders.create_order('1234567812345678123456781234567812345678123456781234567812345678', 1, '2004-07-08', 'packing', '2004-07-08', user1)

    ### Order Products ###
    order_products = []
    for i in range(len(products)):
        prod = product.fetch_product(products[i])
        order_products.append(prod[0])

    ### Reviews ###
    review.create_review(order_products[0], "I don't like coffee", 1, "2025-01-01", user1)
    review.create_review(order_products[0], "I like coffee", 5, "2025-01-01", user2)

    

"""
TODO:
    fixa python funktioner för keyword
    exercisen
    fixa CRUD funktioner
"""