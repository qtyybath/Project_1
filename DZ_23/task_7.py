# запит, який виведе загальні суми продажів для кожного автора та кількість покупок.

# SELECT books.author AS author, COUNT(purchases.book_id) AS amount_sale_units, SUM(books.price) as total_sum_UAH
# FROM purchases
# LEFT JOIN books
# ON purchases.book_id = books.id
# GROUP BY purchases.book_id;


# це варіант для бази з завдання book.store

# SELECT books.author AS author, COUNT(purchase.book_id) AS amount_sale_units, SUM(books.price) as total_sum_UAH
# FROM purchase
# LEFT JOIN books
# ON purchase.book_id = books.id
# GROUP BY purchase.book_id;

