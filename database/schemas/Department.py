from database.Database import Database

class Department:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor()

    def create_department(self, name, desc, parent=None):
        if parent is None:
            self.cursor.execute("""INSERT INTO department (department_name, department_desc) 
                                VALUES (%s, %s);""", (name, desc))
    
        else:
            self.cursor.execute("""INSERT INTO department (department_name, department_desc, parent_department) 
                                VALUES (%s, %s, %s);""", (name, desc, parent))

        self.db.commit()
        return self.cursor.lastrowid

    def get_by_id(self, dep_id):
        pass

    def update(self, dep_id, **fields):
        pass

    def delete(self, dep_id):
        pass

    def list_all(self):
        pass