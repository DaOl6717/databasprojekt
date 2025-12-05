from database.Database import Database
from tasks.task4 import task4
from tasks.task5 import task5
from tasks.create_tables import create_tables
from tasks.prune_tables import prune_tables

def main():
    db = Database()
    db.connect()

    # optional. Will violate unique constraints if running tasks multiple times 
    # without pruning.
    prune_tables(db) 

    create_tables(db)

    task4(db)
    task5(db)

    # order = 1
    # cursor = db.cursor()

    # cursor.execute("CALL add_to_order(1, 10, 1)")

    db.close()

if __name__ == "__main__":
    main()
