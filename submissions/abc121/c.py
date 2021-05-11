# sys.stdin.readline()
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ab = []
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a,b))
ab = sorted(ab)
for c, d in ab:
    if m >= d:
        ans += c*d
        m -= d
    else:
        ans += c*m
        break
print(ans)
