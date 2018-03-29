USE myschemas;
SHOW DATABASES;
SHOW TABLES;
SHOW COLUMNS FROM customers;

SELECT prod_name
FROM products;

SELECT prod_id, prod_name, prod_price
FROM products;

SELECT vend_id
FROM products;

SELECT DISTINCT vend_id
FROM products;

SELECT prod_name
FROM products
LIMIT 5;

SELECT prod_name
FROM products
LIMIT 5,5;

SELECT products.prod_name
FROM myschemas.products;

SELECT prod_name
FROM products;

SELECT prod_name
FROM products
ORDER BY prod_name;

SELECT prod_id, prod_price, prod_name
FROM products
ORDER BY prod_price, prod_name;

SELECT prod_id, prod_price, prod_name
FROM products
ORDER BY prod_price DESC;

SELECT prod_id, prod_price, prod_name
FROM products
ORDER BY prod_price DESC, prod_name;

SELECT prod_price
FROM products
ORDER BY prod_price DESC
LIMIT 1;

SELECT prod_name, prod_price
FROM products
WHERE prod_price = 2.50;

SELECT prod_name, prod_price
FROM products
WHERE prod_name = 'fuses';

SELECT prod_name, prod_price
FROM products
WHERE prod_price < 10;

SELECT prod_name, prod_price
FROM products
WHERE prod_price <= 10;

SELECT vend_id, prod_name
FROM products
WHERE vend_id <> 1003;

SELECT prod_name, prod_price
FROM products
WHERE prod_price BETWEEN 5 AND 10;

SELECT cust_id
FROM customers
WHERE cust_email IS NULL;

SELECT prod_id, prod_price, prod_name
FROM products
WHERE vend_id = 1003 AND prod_price <= 10;

SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1002 OR vend_id = 1003;

SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1002 OR vend_id = 1003 AND prod_price >= 10;

SELECT prod_name, prod_price
FROM products
WHERE (vend_id = 1002 OR vend_id = 1003) AND prod_price >= 10;

SELECT prod_name, prod_price
FROM products
WHERE vend_id IN (1002, 1003)
ORDER BY prod_name;

SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1002 OR vend_id = 1003
ORDER BY prod_name;

SELECT prod_name, prod_price
FROM products
WHERE vend_id NOT IN (1002,1003)
ORDER BY prod_name;

SELECT prod_id, prod_name
FROM products
WHERE prod_name LIKE 'jet%';

SELECT prod_id, prod_name
FROM products
WHERE prod_name LIKE '%anvil%';

SELECT prod_name
FROM products
WHERE prod_name LIKE 's%e';

SELECT prod_id, prod_name
FROM products
WHERE prod_name LIKE '_ ton anvil';

SELECT prod_name
FROM products
WHERE prod_name REGEXP '1000'
ORDER BY prod_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '.000';

SELECT prod_name
FROM products
WHERE prod_name REGEXP '1000|2000'
ORDER BY prod_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '[123] Ton'
ORDER BY prod_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '1|2|3 Ton'
ORDER BY prod_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '[1-5] Ton'
ORDER BY prod_name;

SELECT vend_name
FROM vendors
WHERE vend_name REGEXP '.'
ORDER BY vend_name;

SELECT vend_name
FROM vendors
WHERE vend_name REGEXP '\\.'
ORDER BY vend_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '\\([0-9] sticks?\\)';

SELECT prod_name
FROM products
WHERE prod_name REGEXP '[[:digit:]]{4}'
ORDER BY prod_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '^[0-9\\.]'
ORDER BY prod_name;

SELECT 'hello' REGEXP '[0-9]';

SELECT Concat(vend_name, ' (', vend_country, ')')
FROM vendors
ORDER BY vend_name;

SELECT Concat(RTrim(vend_name), ' (', RTrim(vend_country), ')') AS vend_title
FROM vendors
ORDER BY vend_name;

SELECT prod_id, quantity, item_price
FROM orderitems
WHERE order_num = 20005;

SELECT prod_id,
	   quantity,
       item_price,
       quantity*item_price AS expanded_price
FROM orderitems
WHERE order_num = 20005;

SELECT vend_name, Upper(vend_name) AS vend_name_upcase
FROM vendors
ORDER BY vend_name;

SELECT cust_name, cust_contact
FROM customers
WHERE cust_contact = 'Y. Lie';

SELECT cust_name, cust_contact
FROM customers
WHERE soundex(cust_contact) = soundex('Y Lie');

SELECT cust_id, order_num
FROM orders
WHERE order_date = '2005-09-01';

SELECT cust_id, order_num
FROM orders
WHERE Date(order_date) = '2005-09-01';

SELECT cust_id, order_num
FROM orders
WHERE Date(order_date) BETWEEN '2005-09-01' AND '2005-09-30';

SELECT cust_id, order_num
FROM orders
WHERE Year(order_date) = 2005 AND Month(order_date) = 9;

SELECT AVG(prod_price) AS avg_price
FROM products;

SELECT AVG(prod_price) AS avg_price
FROM products
WHERE vend_id = 1003;

SELECT COUNT(*) AS num_cust
FROM customers;

SELECT COUNT(cust_email) AS num_cust
FROM customers;

SELECT MAX(prod_price) AS max_price
FROM products;

SELECT MIN(prod_price) AS min_price
FROM products;

SELECT SUM(quantity) AS items_ordered
FROM orderitems
WHERE order_num = 20005;

SELECT SUM(item_price*quantity) AS total_price
FROM orderitems
WHERE order_num = 20005;

SELECT AVG(DISTINCT prod_price) AS avg_price
FROM products
WHERE vend_id = 1003;

SELECT COUNT(*) AS num_items,
	   MIN(prod_price) AS price_min,
       MAX(prod_price) AS price_max,
       AVG(prod_price) AS price_avg
FROM products;

SELECT COUNT(*) AS num_prods
FROM products
WHERE vend_id = 1003;

SELECT vend_id, COUNT(*) AS num_prods
FROM products
GROUP BY vend_id;

SELECT cust_id, COUNT(*) AS orders
FROM orders
GROUP BY cust_id
HAVING COUNT(*) >= 2;

SELECT vend_id, COUNT(*) AS num_prods
FROM products
WHERE prod_price >= 10
GROUP BY vend_id
HAVING COUNT(*) >= 2;

SELECT vend_id, COUNT(*) AS num_prods
FROM products
GROUP BY vend_id
HAVING COUNT(*) >= 2;

SELECT order_num, SUM(quantity*item_price) AS ordertotal
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 50;

SELECT order_num, SUM(quantity*item_price) AS ordertotal
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 50
ORDER BY ordertotal;