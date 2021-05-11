# sys.stdin.readline()
import sys
input = sys.stdin.readline

x, a, b = map(int, input().split())
if b-a > x:
    ans = 'dangerous'
elif b-a > 0:
    ans = 'safe'
else:
    ans = 'delicious'
print(ans)
