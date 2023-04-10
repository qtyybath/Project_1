# 3. Написати програму, яка буде повертати факторіал введеного числа,
# використовуючи рекурсію.

num = int(input("Enter the number: "))

def factorial(num: int):
    if num == 0:
        return 1
    if num > 0:
        return num * factorial(num - 1)
    return " "


print(f"Factorial for number", num, ":", factorial(num))


# Для зрівняння факториал в циклу for. Можна через print подивитися послідовність від 1 до заданного числа.
# В циклі, як я зрозуміла, значення чила відповідає кількості циклів. Я так зрозуміла, що через рекурсію
# можна швидко знайти число, а через цикл подивитися послідовність.


n = int(input("Enter the number: "))

value = 1
if n > 0:
    for i in range(1, n + 1):
        value = value * i
        print("Factorial sequence from 1 to", i, ":", value)
if n < 0:
    print("Enter a positive natural number")

