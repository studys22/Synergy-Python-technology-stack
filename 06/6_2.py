x = int(input("X: "))
res = 0
i = 1
while i < x**0.5:
    if x % i == 0:
        res += 1
    i += 1

res *= 2
if x % x**0.5 == 0:
    res += 1

print("The quantity of natural divisors of the number ", x, ": ", res, sep="")
