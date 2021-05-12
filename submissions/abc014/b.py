import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
x = list(bin(x))
del x[0], x[0]
ans = 0

for i in range(len(x)):
    if x[len(x) - i - 1] == '1':
        ans += a[i]

print(ans)
