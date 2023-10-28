def print_list(l, i=0):
    if i >= len(l):
        print("Конец списка")
        return
    print(l[i], end=" ")
    print_list(l, i + 1)


l = [i for i in range(17)]
print_list(l)
