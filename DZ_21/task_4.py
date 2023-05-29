# 4.  Для запиту створення таблиці із завдання 1 змінити first_name та last_name таким чином,
# щоб неможливо було додати вже існуючу комбінацію first_name та last_name.
# Формат здачі:
# Оновлений запит зберегти в окремий файл і запушити на git-репозиторій.


# CREATE TABLE IF NOT EXISTS table_data (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   first_name TEXT NOT NULL CHECK (first_name <> ' '),
#   last_name TEXT NOT NULL CHECK (last_name <> ' '),
#   age INTEGER,
#   UNIQUE (first_name, last_name)
# );

