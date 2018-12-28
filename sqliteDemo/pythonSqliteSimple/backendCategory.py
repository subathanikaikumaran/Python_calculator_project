import sqlite3
from category import Category

conn = sqlite3.connect('pos.db')
# for fresh database
conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE category(
                category_name text,
                description text,
               no_of_item integer
                )""")


def insert_category(cat):
    with conn:
        c.execute("INSERT INTO category VALUES (?,?,?)",
                  (cat.category_name, cat.description, cat.no_of_item))


def get_category_by_name(c_name):
    c.execute("SELECT * FROM category WHERE category_name =? ", (c_name,))
    return c.fetchall()


def get_all_category():
    c.execute("SELECT * FROM category")
    return c.fetchall()


def update_category(cat, no_item):
    with conn:
        c.execute("""UPDATE category SET no_of_item = :no_of_item
        WHERE category_name = :c_name """,
                  {'c_name': cat.category_name, 'no_of_item': no_item})


def remove_category(cat_name):
    with conn:
        c.execute("DELETE FROM category WHERE category_name = :c_name", {'c_name': cat_name})


cat1 = Category('Pen', 'This is pen category', 150)
cat2 = Category('Story Book', 'This category includes all story books', 200)
cat3 = Category('Pencil', 'This category includes all Pencil', 500)

insert_category(cat1)
insert_category(cat2)
insert_category(cat3)

print("all category  \n _________________________ \n", get_all_category())
update_category(cat3, 120)
print("\nedited category  \n _________________________ \n", get_category_by_name('Pencil'))

remove_category('Pen')
print("\nfinal category \n _________________________ \n", get_all_category())


conn.close()






