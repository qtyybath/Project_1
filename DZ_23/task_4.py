# 4.  Написати наступні запити:
# запит, який для кожного user порахує суму всіх покупок.
# Результат має бути представлений у форматі: users.id, users.first_name, users.last_name, total_purchases

# SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases
# FROM purchases
# LEFT JOIN users
# ON purchases.user_id = users.id
# LEFT JOIN books
# ON purchases.book_id = books.id
# GROUP BY user_id;


# це варіант для бази з завдання book.store

# SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases
# FROM purchase
# LEFT JOIN users
# ON purchase.user_id = users.id
# LEFT JOIN books
# ON purchase.book_id = books.id
# GROUP BY user_id;
