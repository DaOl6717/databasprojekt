from database.Database import Database

class OrderProduct:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()

    def add_order_product(self, order_id, product_name, description, price, quantity, product_id=None):
        self.cursor.execute("""INSERT INTO order_product (order_id, product_name, product_description, price, quantity, product_id)
                            VALUES (%s, %s, %s, %s, %s);""", (order_id, product_name, description, price, quantity, product_id))
    
