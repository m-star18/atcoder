# sys.stdin.readline()
import sys
input = sys.stdin.readline

x, a, b = map(int, input().split())
if abs(x-a) > abs(x-b):
    ans = 'B'
else:
    ans = 'A'
print(ans)
