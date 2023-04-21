
# 3. Переписати декоратор із першого завдання,
# щоб він приймав цілочисельний аргумент `times`.
# Стільки разів виконувавати друк назви функції і часу, скільки ‘times’ задано.

import time


def func_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"This function: {func.__name__} was launched at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


data = [6745, 98768, 79847, 98946, 6787, 8467, 86678]


@func_decorator(times=2)
def low_high_sales(x):
    sample = list(filter(lambda i: type(i) is int and i >= 30000, data))
    return sample

print(low_high_sales(data))

@func_decorator(times=3)
def sum_argument(x):
    total = sum(x)
    return total

print(sum_argument(data))