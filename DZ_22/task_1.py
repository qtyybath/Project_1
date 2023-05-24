import sqlite3


with sqlite3.connect("database_1.sqlite") as con:
    cur = con.cursor()
    cur.execute(""" """)

print(cur)

# 1. Написати sql запит, який вибере усі записи із таблиці users старше 30 років.

# -- SELECT * FROM users WHERE age > 30;

