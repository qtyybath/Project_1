# 2. Написати запит, який виведе дату покупки і імʼя користувача, що її здійснив.

# Результат має бути представлений у форматі: purchases.id, purchases.date, user.first_name, user.last_name

# це варіант для бази створенної мною book_store_chytanka.sqlite

# SELECT purchases.id, purchases.date, users.first_name, users.last_name
# FROM purchases JOIN users ON purchases.user_id = users.id;


# це варіант для бази що була завантажена із завдання book.store

# SELECT purchase.id, purchase.date, users.first_name, users.last_name
# FROM purchase JOIN users ON purchase.user_id = users.id;


# це варіант запиту через скріпти Python для бази book.store


import sqlite3
from sqlite3 import Cursor

# with sqlite3.connect("D:/PYTHON/book_store.sqlite") as con:
#     cur = con.cursor()
#     cur.execute(" ")
#
# print(cur)
#
#
# query = ("SELECT purchase.id, purchase.date, users.first_name, users.last_name "
#           "FROM purchase JOIN users ON purchase.user_id = users.id ")
#
# res = cur.execute(query)
# print(res.fetchall())



