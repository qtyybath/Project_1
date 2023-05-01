# 2. Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на *@*.

import re

file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as file:
        file_text = file.read()
        print(file_text)
        pattern = r'\S+@\S+\.\S+'
        emails = re.findall(pattern, file_text)

        for email in emails:
            file_text = re.sub(r'\S+@\S+\.\S+', '*@*', file_text)

    with open(file_name, 'w') as file:
        file.write(file_text)
        print(file_text)

    print("The replacement was successful")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("File opening error", e)
