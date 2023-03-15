# домашнє завдання 1_2_3 (я намагалася використати метод input, але в мене не вийшло)

user_input = "Anna"  # слово вводиться в кавичках "" як текст, незалежно від значення

if user_input.isalpha():
    print("text: " + str(user_input) + " - " + str(len(user_input)) + " letters")
elif user_input.isdigit():
    if int(user_input) % 2 == 0:
        print("even number")
    else:
        print("odd number")
else:
    print("error")


# мій варіант

a = 89       # слово вводиться в форматі тексту в "", або в форматі цифри без ""

if a is str(a):
    print("text length: " + str(len(a)) + " letter")
else:
    if a % 2 == 0:
        print("even number")
    else:
        print("odd number")
