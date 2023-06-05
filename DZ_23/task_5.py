# запит, який виведе кількість покупок книжок для кожного user.
# Результат має бути представлений у форматі: user.id, purchases_count


# SELECT users.id, COUNT(purchases.date) AS purchases_count
# FROM purchases
# LEFT JOIN users
# ON purchases.user_id = users.id
# LEFT JOIN books
# ON purchases.book_id = books.id
# GROUP BY user_id;


# це варіант для бази з завдання book.store

# SELECT users.id, COUNT(purchase.date) AS purchases_count
# FROM purchase
# LEFT JOIN users
# ON purchase.user_id = users.id
# LEFT JOIN books
# ON purchase.book_id = books.id
# GROUP BY user_id;
