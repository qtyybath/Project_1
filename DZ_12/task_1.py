# 1. Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.

import time

def func_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"This function: {func.__name__} was launched at {time.strftime('%Y-%m-%d %H:%M:%S')} ")
        return func(*args, **kwargs)

    return wrapper


data = [6745, 98768, 79847, 98946, 6787, 8467, 86678]

@func_decorator
def low_high_sales(x):
    sample = list(filter(lambda i: type(i) is int and i >= 30000, data))
    return sample

print(low_high_sales(data))

@func_decorator
def sum_argument(x):
    total = sum(x)
    return total

print(sum_argument(data))
