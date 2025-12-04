from database.Database import Database
from tasks.task4 import task4
from tasks.task5 import task5
from tasks.create_tables import create_tables
from tasks.prune_tables import prune_tables

def main():
    db = Database()
    db.connect()

    prune_tables(db) # optional
    create_tables(db)

    task4(db)
    task5(db)

    db.close()

if __name__ == "__main__":
    main()
