m = int(input())
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
l = res = 0
r = n - 1
while l <= r:
    if a[l] + a[r] <= m:
        l += 1
    r -= 1
    res += 1
print(res)
