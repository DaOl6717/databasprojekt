from database.Database import Database
from database.schemas.Department import Department
from database.schemas.Keyword import Keyword
from database.schemas.OrderProduct import OrderProduct
from database.schemas.Orders import Orders
from database.schemas.Product import Product
from database.schemas.Review import Review
from database.schemas.Users import Users

def task5(db: Database):
    cursor = db.cursor()
    ### Welcome text for homepage ###
    query1 = "SELECT department_desc FROM department WHERE parent_department is NULL;"
    cursor.execute(query1)
    description = cursor.fetchall()
    print("Homepage: ", description)

    ### List top level departments ###
    query2 = "SELECT department_name, department_desc FROM department WHERE parent_department = 1"
    cursor.execute(query2)
    root_deps = cursor.fetchall()
    print("Root departments:", root_deps)

    ### List featured products ###
    query3 = "SELECT title, product_description, price_excl_vat FROM product WHERE is_featured = TRUE;"
    cursor.execute(query3)
    featured_products = cursor.fetchall()
    print("Featured products:", featured_products)

    ### List all keyword-related products ###
    product = 3

    query4 = """
    SELECT DISTINCT p2.*
    FROM product AS p1
    JOIN keyword pk1 ON pk1.product_id = p1.id
    JOIN keyword pk2 ON pk2.keyword = pk1.keyword
    JOIN product as p2 ON p2.id = pk2.product_id
    WHERE p1.id = %s AND p2.id <> p1.id;
    """
    # -- Given a product, list all keyword-related products (TODO)
    # CREATE PROCEDURE get_keyword_related_products(IN prod_id INT)
    # READS SQL DATA BEGIN
    # BEGIN
    #     DECLARE kw VARCHAR(30);\
    #     SELECT keyword INTO kw FROM keyword WHERE product_id = prod_id;\
    #     SELECT product_id INTO ??? FROM keyword where kw = keyword;\
    #     SELECT title FROM product WHERE ??? = id;\
    # END;
    cursor.execute(query4, (product,))
    prods = cursor.fetchall()
    print("Keyword-related products:", prods)

    ### List products in department ###
    query5 = """
    CREATE PROCEDURE get_dep_products(IN dep_id INT)
    READS SQL DATA 
    BEGIN 
        SELECT p.*, (SELECT Avg(CAST(r.rating AS FLOAT)) 
                    FROM review r 
                    WHERE r.product_id=p.id) 
                    AS Avg_rating 
        FROM product p 
        WHERE department_id = dep_id;
    END;
    """
    cursor.execute(query5)
    prods = cursor.fetchall()
    print("Products in department:", root_deps)

    ### List all products on sale sorted by discount % ###
    query6 = "SELECT title, discount FROM product WHERE discount > 0 ORDER BY discount DESC;"

    cursor.execute(query6)
    discounted_prods = cursor.fetchall()
    print("Discounted products:", discounted_prods)