from database.Database import Database

class Orders:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()

    def create_order(self, payment_reference, tracking_number, order_date, order_status, last_changed, user_id):
        self.cursor.execute("""INSERT INTO orders (payment_reference, tracking_number, order_date, order_status, last_changed, user_id) VALUES (%s, %s, %s, %s, %s, %s);""", (payment_reference, tracking_number, order_date, order_status, last_changed, user_id))
        
        self.db.commit()
        return self.cursor.lastrowid

    def get_by_id(self, order_id):
        pass

    def update_status(self, order_id, new_status):
        pass

    def delete(self, order_id):
        pass

    def list_all(self):
        pass
