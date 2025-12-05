SELECT * FROM product
SELECT * FROM order_product
CALL add_to_order(1, 1, 2) -- Should not work
SELECT * FROM product
SELECT * FROM order_product
CALL add_to_order(1, 1, 1) -- Should work
SELECT * FROM product
SELECT * FROM order_product