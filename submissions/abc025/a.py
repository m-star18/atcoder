import math

s = sorted(input())
n = int(input())

for i in range(math.ceil(n / 5)):
    for j in range(5):
        if n == i * 5 + j + 1:
            ans = s[i] + s[j]
            break

print(ans)
