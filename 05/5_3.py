x = int(input("X: "))
a = int(input("A: "))
b = int(input("B: "))

if a >= x and b >= x:
    print("2")
elif a >= x and b < x:
    print("Mike")
elif a < x and b >= x:
    print("Ivan")
elif a + b >= x:
    print("1")
else:
    print("0")
