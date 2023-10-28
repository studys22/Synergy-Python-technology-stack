import collections

pets = {}


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    return (
        "год"
        if (age % 10 == 1)
        else (
            "лет"
            if (age % 100) in {12, 13, 14}
            else ("года" if (age % 10) in {2, 3, 4} else "лет")
        )
    )


def pets_list():
    if pets:
        for key in pets.keys():
            print(f"{key}: ", end="")
            read(key)
    else:
        print('"База данных" пуста')


def create():
    nameP = input("Кличка питомца: ")
    typeP = input("Вид питомца: ")
    ageP = int(input("Возраст питомца: "))
    ownerP = input("Владелец питомца: ")
    pet_val = {"Вид питомца": typeP, "Возраст питомца": ageP, "Имя владельца": ownerP}

    deq = collections.deque(pets, maxlen=1)
    if deq:
        last = deq[0] + 1
    else:
        last = 1
    pets[last] = {nameP: pet_val}


def read(ID):
    pet = get_pet(ID)
    if pet == False:
        print(f'Питомца с ID "{ID}" не существует')
    else:
        nameP = list(pet.keys())[0]
        pet_val = list(pet.values())[0]
        age = pet_val["Возраст питомца"]
        print(
            f'Это {pet_val["Вид питомца"]} по кличке "{nameP}". Возраст питомца: {pet_val["Возраст питомца"]} {get_suffix(age)}. Имя владельца: {pet_val["Имя владельца"]}'
        )


def update(ID):
    pet = get_pet(ID)
    if pet == False:
        print(
            f'Невозможно обновить данные о питомце с ID "{ID}", т.к. его не существует'
        )
    else:
        new_age = int(input("Введите новый возраст питомца: "))
        pet_val = list(pet.values())[0]
        pet_val["Возраст питомца"] = new_age


def delete(ID):
    pet = get_pet(ID)
    if pet == False:
        print(f'Невозможно удалить питомца с ID "{ID}", т.к. его не существует')
    else:
        pets.pop(ID)
        print("Удалено")


commands = "Создать, Вывести, Обновить, Прочитать, Удалить, Выйти"
commands_set = set(commands.split(", "))
command = input(f"Команда ({commands}): ")
while command != "Выйти":
    if command == "Создать":
        create()
    elif command == "Вывести":
        pets_list()
    elif command in commands_set:
        ID = int(input("ID питомца: "))
        if command == "Обновить":
            update(ID)
        elif command == "Прочитать":
            read(ID)
        elif command == "Удалить":
            delete(ID)
    else:
        print("Неизвестная команда, попробуйте еще раз")
    command = input(f"\n\nКоманда ({commands}): ")
