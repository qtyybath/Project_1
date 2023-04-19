# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

import datetime

class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{self.timestamp}: {self.message}\n')  # я залишила це дублювання щоб бачити що вводиться в файл.
        self.error_my_custom()

    def error_my_custom(self):
        with open('error.txt', 'a') as f:
            f.write(f'{self.timestamp}: {self.message}\n')

class ValueNotNumber(MyCustomException):
    pass

class ValueLessFiveError(MyCustomException):
    pass

class ValueMoreFiveError(MyCustomException):
    pass


while True:
    try:
        user_number = input("Enter number 5: ")
        if not user_number.isdigit():
            raise ValueNotNumber("You entered not a number")
        user_number = int(user_number)
        if user_number < 5:
            raise ValueLessFiveError("You entered number less 5")
        elif user_number > 5:
            raise ValueMoreFiveError("You entered number more 5")
        break
    except ValueLessFiveError:
        print("You entered number less 5\n")
    except ValueMoreFiveError:
        print("You entered number more 5\n")
    except ValueNotNumber:
        print("You entered not a number")

print("You entered number 5")
