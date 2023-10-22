n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(input()))
a.reverse()
print(*a)
