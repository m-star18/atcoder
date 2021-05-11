import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a+b >= 24:
    ans = (a+b)-24
else:
    ans = a+b
print(ans)
