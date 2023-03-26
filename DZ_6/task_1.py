# завдання 1 Створити функцію, яка призводить аргумент до степені
# і повертає його, степінь теж повинна бути аргументом.

def exponentiate(a, b):
    return a ** b


print(exponentiate(4, 2))
print(exponentiate(3, 6))


# Створити функцію, яка сумує будь-яку кількість аргументів і повертає результат.

def sum_argument(x):
    total = sum(x)
    return total


var_num = [3, 6, 9, 4]
sum_argument(var_num)
print(sum_argument(var_num))
