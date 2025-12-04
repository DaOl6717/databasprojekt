--EXERCISE

-- TASK 0
ALTER TABLE product ADD CONSTRAINT non_negative_stock CHECK (stock_quantity>=0); 

INSERT INTO product (title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES ('Strawberry Milk Magic Sipper', 'Strawberry Flavour!', 4, 0.5, 0.4, 50, FALSE, 7);
INSERT INTO product (title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES ('Chocolate Milk Magic Sipper', 'Milk!', 5, 0.5, 0.4, 50, FALSE, 7);
INSERT INTO product (title, product_description, stock_quantity, vat, discount, price_excl_vat, is_featured, department_id)
VALUES ('Tea', 'Spill the tea', 54, 0.3, 0, 45, FALSE, 7);

-- TASK 1 (Prep)
INSERT INTO users (ssn, phone_number, email_address, user_name, user_address, allows_newsletter) 
VALUES (0405040000, '+000701234567', 'filop.hellbonk@yahoo.com', 'Filop Hellbonk', 'Regementsvägen 420', TRUE);

-- Task 1
START TRANSACTION;
INSERT INTO orders(payment_reference, order_date, order_status, last_changed, total_price, user_id)
VALUES ('1234567812345678123456781234567812345678123456781234567812345678', DATE '2004-07-08', 'packing', DATE '2004-07-08', 1);

--Should not work
INSERT INTO order_product (order_id, product_name, product_description, price, quantity)
VALUES (1, 'Strawberry Milk', 'Strawberry Flavour!', 34, 1);
INSERT INTO order_product (order_id, product_name, product_description, price, quantity)
VALUES (1, 'Chocolate Milk', 'Milk!', 34, 4);
INSERT INTO order_product (order_id, product_name, product_description, price, quantity)
VALUES (1, 'Tea', 'Spill it for ducks sake!', 34, 2);

UPDATE product SET stock_quantity = stock_quantity - 1 WHERE id = 1;
UPDATE product SET stock_quantity = stock_quantity - 6 WHERE id = 2;
UPDATE product SET stock_quantity = stock_quantity - 2 WHERE id = 3;

--Should work
INSERT INTO order_product (order_id, product_name, product_description, price, quantity)
VALUES (1, 'Strawberry Milk', 'Strawberry Flavour!', 34, 1);
INSERT INTO order_product (order_id, product_name, product_description, price, quantity)
VALUES (1, 'Chocolate Milk', 'Milk!', 34, 1);
INSERT INTO order_product (order_id, product_name, product_description, price, quantity)
VALUES (1, 'Tea', 'Spill it for ducks sake!', 34, 1);

UPDATE product SET stock_quantity = stock_quantity - 1 WHERE id = 1;
UPDATE product SET stock_quantity = stock_quantity - 1 WHERE id = 2;
UPDATE product SET stock_quantity = stock_quantity - 1 WHERE id = 3;

-- Either 
COMMIT;
-- Or
ROLLBACK;



-- Task 2 (TODO)
CREATE PROCEDURE read_product (
    IN product_id INT,
    OUT n VARCHAR(50),
    OUT d VARCHAR(100),
    OUT p DECIMAL
)
READS SQL DATA
BEGIN
    SELECT title, product_description, price_excl_vat
    INTO n, d, p
    FROM product
    WHERE id = product_id;\
END;

CREATE PROCEDURE add_to_order(IN order_id INT, IN product_id INT, IN quantity INT)
MODIFIES SQL DATA BEGIN ATOMIC
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Not enough stock!';\
        ROLLBACK;\
    END;\
    DECLARE n VARCHAR(50);\
    DECLARE d VARCHAR(100);\
    DECLARE p DECIMAL;\
    CALL read_product(product_id);\
    INSERT INTO order_product (order_id, product_name, product_description, price, quantity)
    VALUES (order_id, n, d, p, quantity);\
    UPDATE product SET stock_quantity = stock_quantity - quantity WHERE id = quantity;\
END;\;

-- TODO (Task 2 ovan)