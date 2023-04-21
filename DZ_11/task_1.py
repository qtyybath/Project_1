# 1. Додати обробку помилок до коду з завдання №7 про телефонну книгу (тема: “Колекції та структури даних. Part 1”)
# Повинно бути як мінімум два блоки try except, де їх використовувати — вирішуєте самі.


tel_list = [{"Name": "Tom", "Surname": "Hardy", "Phone number": "+49 1626 345 74 63"},
            {"Name": "Megan", "Surname": "Fox", "Phone number": "+49 7685 737 78 37"},
            {"Name": "Amanda", "Surname": "Seyfried", "Phone number": "+49 8766 367 74 63"},
            {"Name": "Adam", "Surname": "Sandler", "Phone number": "+49 5658 756 74 66"}]



def phone_book(tel_list):
    contacts_stats = len(tel_list)
    print(f"In the phone book {contacts_stats} contacts")
    f = {}
    f["Name"] = input("Enter contact name:  ")
    f["Surname"] = input("Enter contact surname: ")
    while True:
        try:
            f["Phone number"] = int(input("Enter contact phone number: "))
            break
        except ValueError:
            print("You didn't enter a number") # помилка якщо не число
    tel_list.append(f)
    print("contact addend")

    delete_list = {"Surname": "  "}
    delete_list["Surname"] = input("To delete contact enter surname: ")

    while True:
        try:
            search_contact = False
            for contact in tel_list:
                if contact['Surname'] == delete_list['Surname']:
                    search_contact = True
                    tel_list.remove(contact)
                    print(f"Contact {contact['Name']} {contact['Surname']} delete")
                    break
            if not search_contact:
                raise ValueError("Surname not found")
            break
        except KeyError:
            print("Contact deletion error")   # мені здається я тут наліпила шопопало
        except ValueError as e:
            print(e)
            break

    import json
    if input("Display a list of contacts?") == "yes":
        for contact in tel_list:
            for key, value in contact.items():
                if key == "Surname":
                    print(value)

    search = input("Enter surname to search: ")
    for contact in tel_list:
        for key, value in contact.items():
            if value == search:
                print(json.dumps(contact, indent=2, separators=(",", ": ")).replace("{", "").replace("}", ""))

    return f"Number of contacts after changes: {contacts_stats}"


print(phone_book(tel_list))
