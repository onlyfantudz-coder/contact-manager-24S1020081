phonebook = []
def add_contact(name, phone):
    contact = {
        'name': name,
        'phone': phone
    }
    phonebook.append(contact)
    print("Đã thêm liên hệ!")
if __name__ == "__main__":
    main()
