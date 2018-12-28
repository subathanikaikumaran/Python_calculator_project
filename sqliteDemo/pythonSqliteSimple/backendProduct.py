import sqlite3
from product import Product

conn = sqlite3.connect('pos.db')
# for fresh database
conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE product(
                product_name text,
                category text,
               product_price integer
                )""")

c.execute("INSERT INTO product VALUES ('Ink Pen','Pen', 12)")

product1 = Product('Red Pen', 'Pen', 15)
product2 = Product('Road to success', 'Story Book', 20)
product3 = Product('HD Pencil', 'Pencil', 13)
# Insert method 1
c.execute("INSERT INTO product VALUES ('{}','{}',{})".
          format(product1.product_name, product1.category, product1.product_price))
conn.commit()

# Insert method 2
c.execute("INSERT INTO product VALUES (?,?,?)", (product2.product_name, product2.category, product2.product_price))
conn.commit()

# Insert method 3
c.execute("INSERT INTO product VALUES (:product_name, :category, :product_price)",
          {'product_name': product3.product_name, 'category': product3.category,
           'product_price': product3.product_price})
conn.commit()

# get all data
c.execute("SELECT * FROM product"); print(c.fetchall())

# get method 1
c.execute("SELECT * FROM product WHERE category = 'Pen' "); print(c.fetchall())

# get method 2
c.execute("SELECT * FROM product WHERE category=?", ('Pen',)); print(c.fetchall())

# get method 3
c.execute("SELECT * FROM product WHERE category=:category", {'category': 'Pen'}); print(c.fetchall())

conn.commit()
conn.close()
