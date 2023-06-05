# 3. Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували, відсортувати дані за user_id.

# Результат має бути представлений у форматі: users.id, users.first_name, users.last_name, books.title

# це варіант для бази створенної мною book_store_chytanka.sqlite

# SELECT users.id, users.first_name, users.last_name, books.title AS title_book
# FROM purchases
# LEFT JOIN users
# ON purchases.user_id = users.id
# LEFT JOIN books
# ON purchases.book_id = books.id
# ORDER BY user_id;


# це варіант для бази з завдання book.store

# SELECT users.id, users.first_name, users.last_name, books.title AS title_book
# FROM purchase
# LEFT JOIN users
# ON purchase.user_id = users.id
# LEFT JOIN books
# ON purchase.book_id = books.id
# ORDER BY user_id;



# це варіант запиту через скріпти Python для бази book.store


import sqlite3

with sqlite3.connect("D:/PYTHON/book_store.sqlite") as con:
    cur = con.cursor()
    cur.execute(" ")

print(cur)


query = ("SELECT users.id, users.first_name, users.last_name, books.title AS title_book "
 "FROM purchase "
 "LEFT JOIN users "
 "ON purchase.user_id = users.id "
 "LEFT JOIN books "
 "ON purchase.book_id = books.id "
 "ORDER BY user_id ")

res = cur.execute(query)
print(res.fetchall())
