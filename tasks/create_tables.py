from database.Database import Database

def create_tables(db: Database):
    statements = ["""
    CREATE TABLE IF NOT EXISTS department(
        id INT AUTO_INCREMENT PRIMARY KEY,
        department_name VARCHAR(50) NOT NULL,
        department_desc VARCHAR(50) NOT NULL,
        parent_department INT,
        FOREIGN KEY (parent_department) REFERENCES department(id)
    );
        """, 
    """
    CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        ssn CHAR(13) UNIQUE NOT NULL,
        phone_number VARCHAR(13) UNIQUE NOT NULL,
        email_address VARCHAR(50) UNIQUE NOT NULL,
        user_name VARCHAR(30) NOT NULL,
        user_address VARCHAR(50) NOT NULL,
        allows_newsletter BOOLEAN NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS product(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(50) NOT NULL,
        product_description VARCHAR(100) NOT NULL,
        stock_quantity INT NOT NULL,
        vat DECIMAL NOT NULL,
        discount FLOAT NOT NULL DEFAULT 0,
        price_excl_vat DECIMAL NOT NULL,
        is_featured BOOLEAN NOT NULL,
        department_id INT NOT NULL,
        FOREIGN KEY (department_id) REFERENCES department(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS review(
        id INT AUTO_INCREMENT NOT NULL,
        product_id INT NOT NULL,
        review_description VARCHAR(50),
        rating INT NOT NULL,
        post_date DATE NOT NULL,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (product_id) REFERENCES product(id),
        CONSTRAINT pk_review PRIMARY KEY (id, product_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS orders(
        id INT AUTO_INCREMENT PRIMARY KEY,
        tracking_number INT UNIQUE,
        payment_reference CHAR(64) UNIQUE NOT NULL,
        order_date DATE NOT NULL,
        order_status VARCHAR(9) NOT NULL,
        last_changed DATE NOT NULL,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        CONSTRAINT is_valid_status CHECK (order_status in ('sent', 'delivered', 'packing'))
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS order_product(
        id INT AUTO_INCREMENT NOT NULL,
        order_id INT NOT NULL,
        product_name VARCHAR(50) NOT NULL,
        product_description VARCHAR(50) NOT NULL,
        price DECIMAL NOT NULL,
        quantity INT NOT NULL,
        product_id INT UNIQUE,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (product_id) REFERENCES product(id),
        CONSTRAINT pk_order_product PRIMARY KEY (id, order_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS keyword(
        keyword VARCHAR(30) NOT NULL,
        product_id INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES product(id),
        CONSTRAINT pk_keyword PRIMARY KEY (keyword, product_id)
    );
    """]

    try:
        for s in statements:
            db.cursor().execute(s)
        db.commit()
    except Exception as e:
        try:
            db.rollback()
        except Exception:
            pass
        print("Error creating tables:", e)
        raise