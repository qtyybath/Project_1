# завдання 1

text = input("Enter your text : ")


for sign in list(text):
    if sign.isdigit():
        if int(sign) == 0:
            print(f"{sign} - null")
        elif int(sign) % 2 == 0:
            print(f"{sign} - even number")
        else:
            print(f"{sign} - odd number")
    elif sign.isalpha():
        if sign.isupper():
            print(f"{sign} - capital letter")
        elif sign.islower():
            print(f"{sign} - small letter")
    elif sign.isspace():
        print("space")
    else:
        print(f"{sign} - symbols")




# ще один вариант тільки для цілих слів. щось не знайшла метода для знаків

text = input("Enter your Word: ")
words = text.split()
for word in words:
    if word.isdigit():
        if int(word) % 2 == 0:
            print(f"{word} - even number")
        else:
            print(f"{word} - odd number")
    elif word.isalpha():
        if word.isupper():
            print(f"{word} - All THE lETTERS IN THE WORD ARE CAPITAL")
        elif word.islower():
            print(f"{word} - all the letters in the word are small")
        elif word.istitle():
            print(f"{word} - The first Letter in the word is capital")
    else:
        print(f"{word} - the Word is incorrect")
