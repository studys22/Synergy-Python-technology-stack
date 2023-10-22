l = list(map(int, input().split()))
s = set()
for a in l:
    print(f'{a}: {"YES" if a in s else "NO"}')
    s.add(a)
