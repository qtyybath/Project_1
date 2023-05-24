# 5. Модифікувати попередній запит таким чином, щоб з отриманого результату вибрати
# тільки ті записи, де значення users більше 1. Результатом має бути таблиця:

    #age  | users

    #52    | 2

    #120  | 2



# запит:

# SELECT age, COUNT(id) AS user
# FROM users
# GROUP BY age
# HAVING user > 1
# ORDER BY user DESC, age ASC