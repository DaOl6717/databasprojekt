-- Uppgift 4

-- Delete all previous products
DELETE FROM product;

-- Create home page (top top department)
insert into department (id, department_name, department_desc) values (0, 'Home page', 'Welcome text for the home page!');

-- Create 2 top level departments
insert into department (id, department_name, department_desc, parent_department) values (1, 'Root 1', 'Call a bondulance', 0);
insert into department (id, department_name, department_desc, parent_department) values (2, 'I am Root 2', 'Call a bondulance', 0);

-- Create 6 child departments
insert into department (id, department_name, department_desc, parent_department) values (3, 'I am 1.1', 'Call a bondulance', 1);
insert into department (id, department_name, department_desc, parent_department) values (4, 'I am 1.2', 'Call a bondulance', 1);
insert into department (id, department_name, department_desc, parent_department) values (5, 'I am 1.3', 'Call a bondulance', 1);

insert into department (id, department_name, department_desc, parent_department) values (6, 'I am 2.1', 'Call a bondulance', 2);
insert into department (id, department_name, department_desc, parent_department) values (7, 'I am 2.2', 'Call a bondulance', 2);
insert into department (id, department_name, department_desc, parent_department) values (8, 'I am 2.3', 'Call a bondulance', 2);

-- Create 10 products
-- Initial product created by hand, copied nine times using AI to reduce repetitive work
INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (1, 'Coffee', 'Freshly brewed coffee', 100, 0.2, 0.05, 50, TRUE, 3);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (2, 'Green Tea', 'Organic green tea leaves', 80, 0.2, 0, 40, FALSE, 3);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (3, 'Tea', 'Spill the tea', 54, 0.3, 0, 45, FALSE, 3);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (4, 'Espresso', 'Strong Italian espresso', 70, 0.2, 0.1, 60, TRUE, 4);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (5, 'Black Tea', 'Rich black tea', 60, 0.2, 0, 35, FALSE, 4);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (6, 'Latte', 'Creamy milk latte', 90, 0.2, 0.05, 55, TRUE, 4);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (7, 'Herbal Tea', 'Relaxing herbal blend', 50, 0.3, 0, 42, FALSE, 5);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (8, 'Cappuccino', 'Frothy cappuccino', 65, 0.2, 0, 58, TRUE, 6);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (9, 'Oolong Tea', 'Premium oolong tea', 40, 0.3, 0.05, 48, FALSE, 7);

INSERT INTO product (id, title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES (10, 'Mocha', 'Chocolate flavored coffee', 75, 0.2, 0, 62, TRUE, 8);

UPDATE product SET discount = 0.05 WHERE id=1;
-- Create 2 users
INSERT INTO users (
	id, 
	ssn, 
	phone_number, 
	email_address, 
	user_name, 
	user_address, 
	allows_newsletter
) 
VALUES 
(1, 0405040000, '+000701234567', 'mario@yahoo.com', 'Filop', 'Address 1', FALSE);

INSERT INTO users (
	id, 
	ssn, 
	phone_number, 
	email_address, 
	user_name, 
	user_address, 
	allows_newsletter
) 
VALUES 
(2, 0407080000, '+000701234568', 'luigi@yahoo.com', 'Davud', 'Address 2', TRUE);

-- Create 2 reviews for the same product
INSERT INTO review (id, product_id, rating, post_date, user_id)
    VALUES (1, 3, 1, DATE '2025-12-01', 1);

INSERT INTO review (id, product_id, rating, post_date, user_id)
    VALUES (2, 3, 5, DATE '2025-11-22', 2);

-- Create one order for one of the users
INSERT INTO orders(
	id, 
	payment_reference, 
	order_date, 
	order_status, 
	last_changed, 
	user_id
)
VALUES (1, '1234567812345678123456781234567812345678123456781234567812345678', DATE '2004-07-08', 'packing', DATE '2004-07-08', 2);
INSERT INTO order_product (id, order_id, product_name, product_description, price, quantity)
VALUES (3, 1, 'Tea', 'Spill the tea', 45, 2);



-- Uppgift 5
-- Get text for the homepage
SELECT department_desc FROM department WHERE id = 0;

-- List of the top level departments with fields needed for the homepage
SELECT department_name, department_desc FROM department WHERE parent_department = 0;

-- List of the featured products with fields needed for the homepage
SELECT title, product_description, price_excl_vat FROM product WHERE is_featured = TRUE;

-- Given a product, list all keyword-related products (TODO)
CREATE PROCEDURE get_keyword_related_products(IN prod_id INT)
READS SQL DATA BEGIN
BEGIN
    DECLARE kw VARCHAR(30);\
    SELECT keyword INTO kw FROM keyword WHERE product_id = prod_id;\
    SELECT product_id INTO ??? FROM keyword where kw = keyword;\
    SELECT title FROM product WHERE ??? = id;\
END;

-- GPT, vi har dock inga keywords inlagda än så kan it testas
SELECT DISTINCT p.id, p.title
FROM product p
JOIN keyword k ON p.id = k.product_id
WHERE k.keyword IN (
    SELECT keyword
    FROM keyword
    WHERE product_id = :prod_id
)
AND p.id <> :prod_id;
-- End of GPT

-- Given a department, list all of their product attributes + average rating
-- OBS DENNA FUNGERAR OM MAN MANUELLT KÖR DELEN MELLAN BEGIN OCH END,
-- MEN VI HAR INTE LYCKATS KÖRA PROCEDURES FÖR MIMER SUGER BALLE (instämmer mvh davud)
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

-- List of all products on sale, sorted by the discount percentage (starting with the biggest discount)
SELECT title, discount FROM product WHERE discount > 0 ORDER BY discount DESC;

-- Uppgift 6 (TODO)
