# 1. Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.


def recursion(num: int):
    print(num)
    if num > 0:
        recursion(num - 1)
    if num < 0:
        recursion(num + 1)
    return None


value_input = recursion(int(input("Enter the number: ")))
print(value_input)
