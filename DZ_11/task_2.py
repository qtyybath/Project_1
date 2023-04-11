# 2.  Написати кастомний Exception клас, MyCustomException, який має повідомляти
# "Custom exception is occurred".

class MyCustomException(Exception):
    pass

class ValueLessFiveError(MyCustomException):
    pass

class ValueMoreFiveError(MyCustomException):
    pass


while True:
    try:
        user_number = int(input("Enter number 5: "))
        if user_number < 5:
            raise ValueLessFiveError
        elif user_number > 5:
            raise ValueMoreFiveError
        break
    except ValueLessFiveError:
        print("You entered number less 5\n")
    except ValueMoreFiveError:
        print("You entered number more 5\n")
    except ValueError:
        print("You entered not a number\n")

print("You entered number 5")

