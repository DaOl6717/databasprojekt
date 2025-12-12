from database.Database import Database

class Keyword:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()
