# 2. Створити програму, яка буде приймати число і друкувати
# відповідне число в послідовності Фібоначчі, використовуючи рекурсію.

num = int(input("Enter the number > 0: "))


def fibonacci(num: int):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(f"Fibonacci for number", num, ":", fibonacci(num))


# доповнила для порівняння циклом while, тут показана послідовність ряду Fibonacci від 2. Я перепробувала варіанти
# щоб вивести через while весь ряд чисел від 1, 1 - але в мене не вийшло ((( тільки від 2, бо в циклі є умова num > 2


num1 = 1
num2 = 1
while num > 2:
    num1, num2 = num2, num1 + num2
    print(num2, end=', ')
    num -= 1



