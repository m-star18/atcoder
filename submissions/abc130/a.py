import sys
input = sys.stdin.readline

x, a = map(int, input().split())
if x >= a:
    ans = 10
else:
    ans = 0
print(ans)
