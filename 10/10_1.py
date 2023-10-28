pets = {}
nameP = input("Кличка питомца: ")
typeP = input("Вид питомца: ")
ageP = int(input("Возраст питомца: "))
ownerP = input("Владелец питомца: ")

pets[nameP] = {"Вид питомца": typeP, "Возраст питомца": ageP, "Имя владельца": ownerP}

for key, val in pets.items():
    ageP = val["Возраст питомца"]
    print(
        f'Это {val["Вид питомца"]} по кличке "{key}". Возраст питомца: {val["Возраст питомца"]} {"год" if (ageP % 10 == 1) else ("лет" if (ageP % 100) in {12, 13, 14} else ("года" if (ageP % 10) in {2, 3, 4} else "лет"))}. Имя владельца: {val["Имя владельца"]}'
    )
