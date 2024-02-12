from phonebook_manager import load_phonebook
from crud_operations import display_entries, add_entry, edit_entry, search_entries, \
    delete_entry


def main():
    phonebook = load_phonebook()
    page_size = 4  # Количество выводов записей
    page_number = 1  # Номер страницы

    while True:
        print("Меню:")
        print("1. Вывести записи из справочника")
        print("2. Добавить новую запись")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Поиск записей")
        print("0. Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            display_entries(phonebook, page_size, page_number)
        elif choice == "2":
            add_entry(phonebook)
        elif choice == "3":
            edit_entry(phonebook)
        elif choice == "4":
            delete_entry(phonebook)
        elif choice == "5":
            search_entries(phonebook)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз")

    print("До свидания!")

if __name__ == "__main__":
    main()