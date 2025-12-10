from database.Database import Database

class Users:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()

    def create_user(self, ssn, phone, email, name, address, allows_newsletter):
        self.cursor.execute("""INSERT INTO users (ssn, phone_number, email_address, user_name, user_address, allows_newsletter) 
                            VALUES (%s, %s, %s, %s, %s, %s)""", (ssn, phone, email, name, address, allows_newsletter))
        self.db.commit()
        return self.cursor.lastrowid

    def get_by_id(self, user_id):
        pass

    def update(self, user_id, **fields):
        pass

    def delete(self, user_id):
        pass

    def list_all(self):
        pass