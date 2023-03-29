# 1. Написати функцію, яка повертає тільки однакові елементи двох множин.


# варіант 1
def intersection(set_1, set_2):
    return set_1.intersection(set_2)


set_1 = {434, 357, 368, 838, 564, 436, 328, 732}
set_2 = {574, 436, 368, 712, 756, 956, 953, 838}

set_intersection = intersection(set_1, set_2)

print(set_intersection)

# варіант 2
print(set_1 & set_2)


# варіант 3
def intersection_set(set_1, set_2):
    num = list(filter(lambda x: x in set_1, set_2))
    return num


print(intersection_set(set_1, set_2))


# 2. Написати функцію, яка повертає тільки унікальні елементи двох множин.

# варіант 1

def union(x, y):
    return x.union(y)

data_1 = {64, 85, 84, 93, 94, 89, 30, 22}
data_2 = {65, 85, 81, 93, 99, 89, 31, 22}


data_union = union(data_1, data_2)
print(data_union)

# варіант 2

print(data_1 | data_2)


# 3. Перетворити всі елементи списку типу string в верхній регістр, використовуючи map.

def upper(text):
    return text.upper()


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

for month in map(upper, months):
    print(month)


# 4.  Вивести всі елементи масиву, які є числом, використовуючи filter.

# варіант 1
data = [9, 7, 8, "apple", "pear", 6, 10]


def data_number(data_in):
    out_filter = list(filter(lambda i: type(i) is int, data_in))
    return out_filter

print(data_number(data))
