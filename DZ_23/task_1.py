# 1. Для обліку інформації про користувачів, книжки, видавництва та продажі створити наступні таблиці:

# users: id, first_name, last_name, age

# publishing_house: id, name, rating (default 5)

# books: id, title, author, year, price, publishing_house_id

# purchases: id, user_id, book_id, date

# При цьому:
#
# publishing_house_id — це FOREIGN KEY таблиці publishing_houses
#
# user_id —  це FOREIGN KEY таблиці users
#
# book_id —  це FOREIGN KEY таблиці books


# Варіант 1. я створила таблиці в БД через конструктор Table, а не через консоль.
# Через консоль sqlite внесла в таллиці свої данні, окрім таблиі purchases, я цю таблицю взяла з прикладу,
# але замінила там дати
# таблиці для контролю зберегла в sql файлах


import sqlite3


with sqlite3.connect("book_store_chytanka.sqlite") as con:
    cur = con.cursor()
    cur.execute(""" """)

print(cur)



# CREATE TABLE users
# (
#     id         integer not null
#         primary key autoincrement,
#     first_name text    not null,
#     last_name  text    not null,
#     age        integer not null
# )


# INSERT INTO users (first_name, last_name, age) VALUES ('Amanda', 'Seyfried', 39),
#                                                       ('Megan', 'Fox', 37),
#                                                       ('Katy', 'Perry', 38),
#                                                       ('Tom', 'Hiddleston', 42),
#                                                       ('Leonardo', 'DiCaprio', 48 ),
#                                                       ('Jennifer', 'Aniston', 54);


# CREATE TABLE publishing_houses
# (
#     id     integer     not null
#        primary key autoincrement,
#        name   text not null,
#     rating integer not null default 5
# );

#
# INSERT INTO publishing_houses (name, rating) VALUES ('Fabula', 4),
#                                                   ('Bookchef', 3 ),
#                                                 ('Lingvist', 5 );

# CREATE TABLE books
# (
#     id                  integer not null
#         primary key autoincrement,
#     title               text    not null,
#     author              text    not null,
#     year                integer not null,
#     price               integer not null,
#     publishing_house_id integer
# );
#
#
#
# INSERT INTO books (title, author, year, price , publishing_house_id)
# VALUES ('Dpublishing_house_idune', 'Frank Herbert', 2019, 800, 1),
# ('Blindsight', 'Peter Watts', 2019, 800, 3),
# ('The Three-Body Problem', 'liu Cixin', 2020, 900, 4),
# ('Hyperion ', 'Dan simmons', 2015, 700, 2),
# ('American Gods', 'Neil Gaiman', 2017, 1000, 4),
# ('1984 ', 'George Orwell', 2015, 700, 1),
# ('The Colour of Magic', 'Terry Pratchett', 2017, 1000, 3);


# CREATE TABLE "purchases"
# (
#     id      integer,
#     user_id integer,
#     book_id integer,
#     date    text
# )



# Варіант 2. приклад створення таблиць в БД через скріпти Python.

# query = ("CREATE TABLE IF NOT EXISTS users ("
#          "id integer not null primary key autoincrement, "
#           "first_name text    not null, "
#           "last_name  text    not null, "
#           "age  integer not null)")
#
# cur.execute(query)
#
# query = ("INSERT INTO users (first_name, last_name, age) "
#          "VALUES ('Amanda', 'Seyfried', 39) ,"
#                 "('Megan', 'Fox', 37), "
#                 "('Katy', 'Perry', 38), "
#                 "('Tom', 'Hiddleston', 42), "
#                 "('Leonardo', 'DiCaprio', 48 ), "
#                 "('Jennifer', 'Aniston', 54)")
#
# cur.execute(query)
# con.commit()


# query = ("CREATE TABLE publishing_houses ("
#     "id     integer     not null "
#     "primary key autoincrement, "
#      "name   text not null, "
#     "rating integer not null default 5)")
#
# cur.execute(query)
#
#
# data = [
#     ('Fabula', 4),
#     ('Bookchef', 3),
#     ('Lingvist', 5),
#      ]
#
# query = "INSERT INTO publishing_houses (name, rating) VALUES (?, ?)"
#
# cur.executemany(query, data)
# con.commit()

# query = ("CREATE TABLE IF NOT EXISTS books ("
#          "id integer not null "
#          "primary key autoincrement, "
#          "title               text    not null, "
#          "author              text    not null, "
#          "year                integer not null, "
#          "price               integer not null, "
#          "publishing_house_id integer)")
#
# cur.execute(query)
#
# query = ("INSERT INTO books (title, author, year, price , publishing_house_id) "
#     "VALUES ('Dpublishing_house_idune', 'Frank Herbert', 2019, 800, 1), "
#     "('Blindsight', 'Peter Watts', 2019, 800, 3), "
#     "('The Three-Body Problem', 'liu Cixin', 2020, 900, 4), "
#     "('Hyperion ', 'Dan simmons', 2015, 700, 2), "
#     "('American Gods', 'Neil Gaiman', 2017, 1000, 4), "
#     "('1984 ', 'George Orwell', 2015, 700, 1), "
#     "('The Colour of Magic', 'Terry Pratchett', 2017, 1000, 3)")
#
# cur.execute(query)
# con.commit()


# query = ("CREATE TABLE purchases ("
#     "id      integer not null "
#     "primary key autoincrement, "
#     "user_id integer, "
#     "book_id integer, "
#     "date    text)")
#
# cur.execute(query)


# data = [
#         (1, 1, '2023.01'),
#         (5, 2, '2023.01'),
#         (2, 1, '2023.01'),
#         (1, 3, '2023.03'),
#         (5, 5, '2023.04'),
#         (3, 3, '2023.03'),
#         (6, 2, '2023.01'),
#         (6, 3, '2023.03'),
#         (4, 4, '2023.05'),
#         (4, 1, '2023.01'),
#         (5, 3, '2023.03'),
#         (3, 4, '2023.02'),
#         (2, 5, '2023.04'),
#         (3, 1, '2023.01'),
#         (2, 2, '2023.01'),
#         (3, 2, '2023.01'),
#         (4, 6, '2023.02'),
#         (1, 7, '2023.05'),
#         (2, 6, '2023.04'),
#         (6, 5, '2023.02'),
#      ]
#
# query = "INSERT INTO purchases (user_id, book_id, date ) VALUES (?, ?, ?)"
#
# cur.executemany(query, data)
# con.commit()