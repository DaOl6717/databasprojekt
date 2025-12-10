from database.Database import Database

class Product:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()

    def create_product(self, title, description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id):
        self.cursor.execute("""INSERT INTO product (title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""", (title, description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id))
        self.db.commit()
        return self.cursor.lastrowid

    def fetch_product(self, product_id):
        query = "SELECT * FROM product WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()

    def update(self, product_id, **fields):
        pass

    def delete(self, product_id):
        pass

    def list_all(self):
        pass
    
    def list_products_in_department(self, department_id):
        query = "SELECT * FROM product WHERE department_id=%s"
        self.cursor.execute(query, (department_id,))
        
        products = self.cursor.fetchall()
        return products
                                    