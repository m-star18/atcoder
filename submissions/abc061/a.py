import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
if (a <= c) and (b >= c):
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
