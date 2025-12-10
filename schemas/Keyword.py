from database.Database import Database

class Keyword:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()

    def add_keyword(self, keyword, product_id):
        pass

    def remove(self, keyword, product_id):
        pass

    def list_for_product(self, product_id):
        pass
