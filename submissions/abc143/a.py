import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a > b * 2:
    ans = a - b * 2
else:
    ans = 0
print(ans)
