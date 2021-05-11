# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if (a*b)%2 == 0:
    ans = 'Even'
else:
    ans = 'Odd'
print(ans)
