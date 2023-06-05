# запит, який виведе кількість покупок книжок для автора Rowling.
# Результат має бути представлений у форматі: amount

# я зробила в двах варіантах
#  але є зауваження. чомусь PYcharm підсвічував HAVING, хоча запит видало правильно, без error.
#  не розумію в чому помилка

# SELECT books.author AS author, COUNT(purchases.book_id) AS amount
# FROM purchases
# LEFT JOIN books
# ON purchases.book_id = books.id
# GROUP BY purchases.book_id
# HAVING purchases.book_id = 1

# SELECT books.author AS author, COUNT(purchases.book_id) AS amount
# FROM purchases
# LEFT JOIN books
# ON purchases.book_id = books.id
# GROUP BY books.author
# HAVING books.author= 'Frank Herbert';



# це варіант для бази з завдання book.store

# SELECT books.author AS author, COUNT(purchase.book_id) AS amount
# FROM purchase
# LEFT JOIN books
# ON purchase.book_id = books.id
# GROUP BY purchase.book_id
# HAVING purchase.book_id = 1
