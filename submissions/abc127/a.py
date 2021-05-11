# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a >= 6:
    if a >= 13:
        ans = b
    else:
        ans = int(b/2)
else:
    ans = 0
print(ans)
