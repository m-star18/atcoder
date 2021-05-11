# sys.stdin.readline()
import sys
input = sys.stdin.readline

x, t = map(int, input().split())
if x <= t:
    ans = 0
else:
    ans = x-t
print(ans)
