# 1. Створити базу даних SQLite. Використовуючи SQL запити, в створеній базі даних створити таблицю,
# яка має містити наступні поля:
# id - значення для кожного нового елементу має за замовчуванням бути +1 від попереднього
# first_name — текстове значення
# last_name — текстове значення
# age — число
# Формат здачі:
# Зберегти запит для створення таблиці в файл і запушити на git-репозиторій.


import sqlite3

with sqlite3.connect("base_one.sqlite") as con:
    cur = con.cursor()
    cur.execute(""" """)

print(cur)



# запит для створення таблиці

# CREATE TABLE table_name
# (
#     id         integer not null
#         primary key autoincrement,
#     first_name text    not null,
#     last_name  text    not null,
#     age        int     not null
# )

# я створила таблицю через конструктор, а не через запит. як ви показували на занятті
# просто витягнула вже автоматично створений запит


