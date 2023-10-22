def back_to_top(a: list):
    a.insert(0, a[-1])
    a.pop()


n = int(input("N: "))
a = list(map(int, input().split()))
back_to_top(a)
print(*a)
