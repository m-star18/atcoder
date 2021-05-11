import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
if a%2 == 1 and b%2 == 1 and c%2 == 1:
    ans = min(a*b, b*c, a*c)
else:
    ans = 0
print(ans)
