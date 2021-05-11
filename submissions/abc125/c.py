import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

n, *a = map(int, read().split())
b = a[::-1]
cumsum_m = [0] * (n - 1)
cumsum_p = [0] * (n - 1)
cumsum_m[0] = b[0]
cumsum_p[0] = a[0]
for i in range(1, n - 1):
    cumsum_p[i] = gcd(cumsum_p[i - 1], a[i])
    cumsum_m[i] = gcd(cumsum_m[i - 1], b[i])
ans = max(cumsum_m.pop(), cumsum_p.pop())
for p, m in zip(cumsum_p, cumsum_m[::-1]):
    v = gcd(p, m)
    if ans < v:
        ans = v
print(ans)
