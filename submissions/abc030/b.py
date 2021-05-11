import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n >= 12:
    n -= 12

ans = abs((m - (n * 5 + (m * 5) / 60)) * 6)

if ans > 180:
    ans = abs(360 - ans)

print(ans)
