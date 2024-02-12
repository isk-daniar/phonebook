import json


# Файл для хранения данных справочника
PHONEBOOK_FILE = "phonebook.txt"


def load_phonebook():
    try:
        with open(PHONEBOOK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, "w") as file:
        json.dump(phonebook, file)
