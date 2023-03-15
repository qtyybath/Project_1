# завдання зробила без перевірки, бо в мене не стоїть версія 3.10


a = "Anna"

match a:
    case str(y):
        print("text")
    case int(y):
        print("integer")
    case float(y):
        print("dotted number")
    case _:
        print('unknown')

