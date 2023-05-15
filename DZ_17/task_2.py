# 3.  Створити клас MyStr(str), який має перевизначтити метод str таким чином,
# щоб замість друку реального значення всі літери були переведені в верхній регістр:

class MyStr(str):
    def __str__(self):
        return super().__str__().upper()


my_str = MyStr('test')
print(my_str)
