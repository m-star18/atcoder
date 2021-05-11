import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a+b >= 10:
    ans = 'error'
else:
    ans = a+b
print(ans)
