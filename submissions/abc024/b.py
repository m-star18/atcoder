import sys
input = sys.stdin.readline

n, t = map(int, input().split())
ans = 0
a = [0] * n
a[0] = int(input())
for i in range(1, n):
    a[i] = int(input())
    if a[i] - a[i - 1] >= t:
        ans += t
    else:
        ans += a[i] - a[i - 1]

print(ans + t)
