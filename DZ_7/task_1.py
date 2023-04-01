# Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів
# add: додати запис
# delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі
# show <name>: детальна інформація по імен

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
    f["Phone number"] = input("Enter  contact phone number: ")
    tel_list.append(f)
    print("contact addend")

    delete_list = {}
    if input("Delete contact?") == "yes":
        delete_list["Surname"] = input("Enter contact surname: ")

        delete_surname = delete_list["Surname"]
        print(delete_surname)

        for contact in tel_list:
            for key, value in contact.items():
                if value == delete_surname:
                    tel_list.pop(tel_list.index(contact))
    print("Contact removed")

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


# получилося не ідеально, бо треба детально прописувати багато if, але здається основні задачі завдання програма віконує

