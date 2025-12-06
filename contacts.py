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
def view_contacts():
    if len(phonebook) == 0:
        print("Danh bạ đang trống.")
    else:
        print("\n--- Danh bạ ---")
        for contact in phonebook:
            print(f"Tên: {contact['name']} - SĐT: {contact['phone']}")
def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Thêm liên hệ mới")
        print("2. Hiển thị danh bạ")
        print("3. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            name = input("Nhập tên: ")
            phone = input("Nhập số điện thoại: ")
            add_contact(name, phone)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ!")
