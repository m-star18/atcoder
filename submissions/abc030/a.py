import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())

if b / a > d / c:
    ans = 'TAKAHASHI'

elif b / a == d / c:
    ans = 'DRAW'

else:
    ans = 'AOKI'

print(ans)
