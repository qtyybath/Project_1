# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл)
# і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.

tel_list = [{"Name": "Tom", "Surname": "Hardy", "Phone number": "+49 1626 345 74 63"},
            {"Name": "Megan", "Surname": "Fox", "Phone number": "+49 7685 737 78 37"},
            {"Name": "Amanda", "Surname": "Seyfried", "Phone number": "+49 8766 367 74 63"},
            {"Name": "Adam", "Surname": "Sandler", "Phone number": "+49 5658 756 74 66"}]

import json

try:
    with open("tele_data.txt", "x") as f:       # я створила файл спочатку, загрузила дані. це працює один раз спочатку
        json.dump(tel_list, f)
except FileExistsError:
    print("File already exists!")

try:
    with open("tele_data.txt", "r") as file:  # відкрила файл для читання і роботи з даними, це працює після запуску
        data = file.read()
        tele_data = json.loads(data)
        print(type(tele_data))
        print(tele_data)
except:
    print("Problem opening file!")

def phone_book(tele_data):
    contacts_stats = len(tele_data)
    print(f"In the phone book {contacts_stats} contacts")
    f = {}
    f["Name"] = input("Enter contact name:  ")
    f["Surname"] = input("Enter contact surname: ")
    while True:
        try:
            f["Phone number"] = int(input("Enter contact phone number: "))
            break
        except ValueError:
            print("You didn't enter a number")
    tele_data.append(f)
    print("Contact added")
    print(tele_data)

    delete_list = {"Surname": "  "}
    delete_list["Surname"] = input("To delete contact enter surname: ")

    while True:
        try:
            search_contact = False
            for contact in tele_data:
                if contact['Surname'] == delete_list['Surname']:
                    search_contact = True
                    tele_data.remove(contact)
                    print(f"Contact {contact['Name']} {contact['Surname']} delete")
                    break
            if not search_contact:
                raise ValueError("Surname not found")
            break
        except KeyError:
            print("Contact deletion error")
        except ValueError as e:
            print(e)
            break

    try:
        with open("tele_data.txt", "w") as file:  # перезаписала дані після додавання та видалення контактів, працює після змін
            json.dump(tele_data, file)
            print(type(tele_data))
    except:
        print("Problem opening file!")

    if input("Display a list of contacts?") == "yes":
        for contact in tele_data:
            for key, value in contact.items():
                if key == "Surname":
                    print(value)

    search = input("Enter surname to search: ")
    for contact in tele_data:
        for key, value in contact.items():
            if value == search:
                print(json.dumps(contact, indent=2, separators=(",", ": ")).replace("{", "").replace("}", ""))

    return f"Number of contacts after changes: {len(tele_data)}"


print(phone_book(tele_data))
