import sys
input = sys.stdin.readline

l, r = map(int, input().split())
if r - l > 2019:
    ans = 0
else:
    ans = float('inf')
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            ans = min(ans, (i * j) % 2019)
print(ans)
