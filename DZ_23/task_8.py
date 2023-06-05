# запит, який виведе всі назви книжок із кількістю їх продажів в порядку спадання кількості продажів.

# SELECT books.title AS title, COUNT(purchases.book_id) AS amount_sale_units
# FROM purchases
# LEFT JOIN books
# ON purchases.book_id = books.id
# GROUP BY purchases.book_id
# ORDER BY amount_sale_units DESC ;



# це варіант для бази з завдання book.store

# SELECT books.title AS title, COUNT(purchase.book_id) AS amount_sale_units
# FROM purchase
# LEFT JOIN books
# ON purchase.book_id = books.id
# GROUP BY purchase.book_id
# ORDER BY amount_sale_units DESC ;