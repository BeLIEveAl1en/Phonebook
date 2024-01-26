def read_txt(filename):
    phone_book = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                last_name, first_name, middle_name, phone_number = line.strip().split(',')
                phone_book.append({'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name,
                                   'phone_number': phone_number})
    except FileNotFoundError:
        print("Файл не найден. Создайте новый справочник.")
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w') as file:
        for record in phone_book:
            file.write(
                f"{record['last_name']},{record['first_name']},{record['middle_name']},{record['phone_number']}\n")


def print_result(phone_book):
    for record in phone_book:
        print(f"{record['last_name']} {record['first_name']} {record['middle_name']}: {record['phone_number']}")


def find_by_lastname(phone_book, last_name):
    found_records = [record for record in phone_book if record['last_name'] == last_name]
    return found_records if found_records else "Записи с такой фамилией не найдены."


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['last_name'] == last_name:
            record['phone_number'] = new_number
            return "Номер телефона успешно изменен."
    return "Запись с такой фамилией не найдена."


def delete_by_lastname(phone_book, last_name):
    phone_book[:] = [record for record in phone_book if record['last_name'] != last_name]
    return "Запись успешно удалена."


def find_by_number(phone_book, number):
    found_records = [record for record in phone_book if record['phone_number'] == number]
    return found_records if found_records else "Записи с таким номером не найдены."


def add_user(phone_book, user_data):
    try:
        last_name, first_name, middle_name, phone_number = user_data.split(',')
        phone_book.append({'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name,
                           'phone_number': phone_number})
        print("Новая запись успешно добавлена.")
    except ValueError:
        print(
            "Ошибка в формате ввода данных. Пожалуйста, введите данные в формате 'Фамилия,Имя,Отчество,Номер телефона'.")


def show_menu():
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Найти записи по фамилии")
    print("3. Изменить номер телефона")
    print("4. Удалить запись по фамилии")
    print("5. Найти записи по номеру телефона")
    print("6. Добавить новую запись")
    print("7. Выйти")
    return int(input("Выберите действие: "))


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер телефона: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите данные новой записи (Фамилия,Имя,Отчество,Номер телефона): ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)

        choice = show_menu()


work_with_phonebook()
