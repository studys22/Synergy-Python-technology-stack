a = int(input("Enter a 5-digit number: "))
a5 = a % 10
a //= 10
a4 = a % 10
a //= 10
a3 = a % 10
a //= 10
a2 = a % 10
a1 = a // 10

print("Solution:", a4**a5 * a3 / (a1 - a2))
