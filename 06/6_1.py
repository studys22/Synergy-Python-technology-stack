n = int(input("N: "))
cnt = 0
for i in range(n):
    a = int(input())
    if a == 0:
        cnt += 1

print("The quantity of numbers equal to 0:", cnt)