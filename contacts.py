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
def add_contact(name, phone):
    contact = {
        'name': name,
        'phone': phone
    }
    phonebook.append(contact)
    print("Đã thêm liên hệ!")
elif choice == '1':
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    add_contact(name, phone)
