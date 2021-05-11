import sys
input = sys.stdin.readline

w, a, b = map(int, input().split())
if a < b:
    if b-(a+w) < 0:
        ans = 0
    else:
        ans = b-(a+w)
else:
    if a-(b+w) < 0:
        ans = 0
    else:
        ans = a-(b+w)
print(ans)
