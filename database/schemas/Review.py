from database.Database import Database

class Review:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()

    def create_review(self, product_id, desc, rating, post_date, user_id):
        self.cursor.execute("""INSERT INTO review (product_id, review_description, rating, post_date, user_id)
                            VALUES (%s, %s, %s, %s, %s);""", (product_id, desc, rating, post_date, user_id))
        
        self.db.commit()
        return self.cursor.lastrowid

    def get_by_id(self, review_id):
        pass

    def list_by_product(self, product_id):
        pass

    def delete(self, review_id):
        pass