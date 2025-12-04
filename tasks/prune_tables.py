from database.Database import Database

def prune_tables(db: Database):
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS department, users, product, review, orders, order_product, keyword;")
        db.commit()