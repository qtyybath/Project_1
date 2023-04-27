# 3. Написати програму, яка буде:
#зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
#знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери
# справжньої адреси, а весь інший текст має бути замінений на *. Кількість * необовʼязково
# має відповідати кількості замінених символів

import re

file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as file:
        file_text = file.read()
        print(file_text)
        pattern = r'\b(\w)[\w.]+(@\w+\.\w{2,})\b'
        search_text = re.findall(pattern, file_text)
        print(search_text)


        def replace(search_text):
            first_char = search_text.group(1)
            last_char = search_text.group(2)[-1]
            return f'{first_char}****@****{last_char}'
        new_text = re.sub(pattern, replace, file_text)

        print(new_text)

    with open(file_name, 'w') as file:
        file.write(new_text)

    print("The replacement was successful")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("File opening error", e)

