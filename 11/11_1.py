def factorial(n):
    res = 1
    for i in range(n):
        res *= i + 1
    return res


n = int(input("Enter a natural number: "))
res = []
for i in range(factorial(n), 0, -1):
    res.append(factorial(i))
print(res)
