# 3. Знайти найбільший елемент масиву
# — використати built-in функцію
# — створити свою функцію
# — використати лямбда функцію

# рішення: з допомогою встроєної функції max знайдено елемент з максимальним значенням

values_variant = [346, 848, 759, 70474, 757, 7768]
number_max = max(values_variant)

print(number_max)


# спочатку створено функцію, яка визивається для знайдення максимального значеня


def max_numer(y):
    sort_values = sorted(values_variant)
    return sort_values[-1]


print(max_numer(values_variant))


# зішення через Lamdba в одну строку

max_num = print(max(values_variant, key=lambda x: x))


