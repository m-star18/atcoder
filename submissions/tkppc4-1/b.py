import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans, max = -1, 0
for i in range(n):
    if k > a[i] > max:
        ans = i + 1
        max = a[i]
print(ans)
