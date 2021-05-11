# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
if a+b > c+d:
    ans = 'Left'
elif a+b == c+d:
    ans = 'Balanced'
else:
    ans = 'Right'
print(ans)
