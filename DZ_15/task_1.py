# 1. До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX

tel_list = [{"Name": "Tom", "Surname": "Hardy", "Phone number": "+380504658574"},
            {"Name": "Megan", "Surname": "Fox", "Phone number": "380674663546"},
            {"Name": "Amanda", "Surname": "Seyfried", "Phone number": "+380973648475"},
            {"Name": "Adam", "Surname": "Sandler", "Phone number": "0502364657"}]

import re

import json

def find_phone_number(x):
    re_pattern = r'\+?\d{9,12}'    # пишу патерн
    phone_number = []    # список під пошуковий результат
    if input("Find all phone numbers?") == "yes":    # команда на пошук
        for contact in tel_list:           # ітерую через цикл
            for key, value in contact.items():
                if re.findall(re_pattern, str(value)):      # пошук
                    phone_number.extend(re.findall(re_pattern, str(value)))  # додаю результати пошуки в лист
        return json.dumps(phone_number, indent=0, separators=(",", ": ")).replace("[", " ").replace("]", " ").replace('"', ' ').replace(",", " ")
        # повертаю лист з результатом


print(f"List of phone numbers found: {find_phone_number(tel_list)}")    # запускаю функцію