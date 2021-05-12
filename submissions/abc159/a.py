import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0
for i in range(n):
    ans += i
for j in range(m):
    ans += j
print(ans)
