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

    def update_discount(self, product_id, new_discount):

        nd = float(new_discount)
        if nd > 1:
            nd = nd / 100.0

        nd = max(0, min(1, nd))
        query = "UPDATE product SET discount=%s WHERE id=%s"
        self.cursor.execute(query, (nd, product_id))
        self.db.commit()
        return nd

    def list_products_in_department(self, department_id):
        query = "SELECT id, title, vat, discount, price_excl_vat FROM product WHERE department_id=%s"
        self.cursor.execute(query, (department_id,))
        
        products = self.cursor.fetchall()
        return products

    def calculate_price(self, price_info): #price_excl_vat, vat, discount):
        price_excl_vat, vat, discount = map(float, price_info)

        if discount > 1:
            discount = discount / 100.0

        return (price_excl_vat * (1 + vat) * (1 - discount))
    