from phonebook_manager import save_phonebook


# Отображение запись
def display_entries(phonebook, page_size, page_number):
    start_index = (page_number - 1) * page_size  # Вычисление индексы начала и \
    end_index = start_index + page_size  # конца для выборки записей из справочника на основе размера страницы и номера страницы
    entries = phonebook[start_index:end_index]  # Извлекаем подмножество записей из справочника с помощью среза

    for entry in entries:
        print("Фамилия:", entry.get("фамилия"))
        print("Имя:", entry.get("имя"))
        print("Отчество:", entry.get("отчество"))
        print("Название организации:", entry.get("название организации"))
        print("Рабочий телефон:", entry.get("телефон рабочий"))
        print("Личный телефон:", entry.get("телефон личный"))
        print("--------------------")


# Добавление запись
def add_entry(phonebook):
    entry = {}
    entry["фамилия"] = input("Введите фамилию: ")
    entry["имя"] = input("Введите имя: ")
    entry["отчество"] = input("Введите отчество: ")
    entry["название организации"] = input("Введите название организации: ")
    entry["телефон рабочий"] = input("Введите рабочий телефон: ")
    entry["телефон личный"] = input("Введите личный телефон: ")

    phonebook.append(entry)
    save_phonebook(phonebook)
    print("Запись добавлена в справочни")


# Редактирование записи
def edit_entry(phonebook):
    last_name = input("Введите фамилию записи, которую хотите отредактировать: ")
    matching_entries = []

    for entry in phonebook:
        if entry.get("фамилия") == last_name:
            matching_entries.append(entry)

    if len(matching_entries) == 0:
        print("Запись не найдена")
        return

    print("Найденные записи:")
    for i, entry in enumerate(matching_entries):
        print(f"{i+1}. {entry.get('фамилия')} {entry.get('имя')}")

    entry_number = int(input("Введите номер записи для редактирования: ")) - 1

    if entry_number <= 1 or entry_number >= len(matching_entries):
        print("Неверный номер записи")
        return

    entry = matching_entries[entry_number]

    entry["фамилия"] = input("Введите фамилию: ")
    entry["имя"] = input("Введите имя: ")
    entry["отчество"] = input("Введите отчество: ")
    entry["название организации"] = input("Введите название организации: ")
    entry["телефон рабочий"] = input("Введите рабочий телефон: ")
    entry["телефон личный"] = input("Введите личный телефон: ")

    save_phonebook(phonebook)
    print("Запись отредактирована")


# Удаление записи
def delete_entry(phonebook):
    last_name = input("Введите фамилию записи, которую хотите удалить: ")
    matching_entries = []

    for entry in phonebook:
        if entry.get("фамилия") == last_name:
            matching_entries.append(entry)

    if len(matching_entries) == 0:
        print("Запись не найдена.")
        return

    print("Найденные записи:")
    for i, entry in enumerate(matching_entries):
        print(f"{i+1}. {entry.get('фамилия')} {entry.get('имя')}")

    entry_number = int(input("Введите номер записи для удаления: ")) - 1

    if entry_number < 0 or entry_number >= len(matching_entries):
        print("Неверный номер записи")
        return

    entry = matching_entries[entry_number]
    phonebook.remove(entry)
    save_phonebook(phonebook)
    print("Запись удалена из справочника")


# Поиск записей по фамилии, имени и названию организации
def search_entries(phonebook):
    print("Если не знаете или забыли можете пропустить при помощи кнопки \"Enter\" ")
    last_name = input("Введите фамилию для поиска: ")
    first_name = input("Введите имя для поиска: ")
    organization = input("Введите название организации для поиска: ")
    results = []

    for entry in phonebook:
        if (last_name and entry.get("фамилия") == last_name) or \
                (first_name and entry.get("имя") == first_name) or \
                    (organization and entry.get("название организации") == organization):
                    results.append(entry)

    if len(results) == 0:
        print("Записи не найдены")
        return

    print("Результаты поиска:")
    for i, entry in enumerate(results):
        print(f"{i+1}. {entry.get('фамилия')} {entry.get('имя')}")
        print("Название организации:", entry.get("название организации"))
        print("Рабочий телефон:", entry.get("телефон рабочий"))
        print("Личный телефон:", entry.get("телефон личный"))
        print("--------------------")