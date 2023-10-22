a = int(input("A: "))
b = int(input("B: "))

if a % 2 == 1:
    a += 1
if b % 2 == 1:
    b -= 1
print(*range(a, b + 1, 2))
