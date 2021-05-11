import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a+0.5 <= b:
    ans = '0'
else:
    ans = '1'
print(ans)
