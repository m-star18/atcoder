import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, read().split())
mod = 10 ** 9 + 7
memo = [0] * (k + 1)
ans = 0
for x in range(k, 0, -1):
    v = k // x
    tmp = pow(v, n, mod)
    for i in range(2, v + 1):
        tmp -= memo[i * x]
        tmp %= mod
    memo[x] = tmp
for i, vv in enumerate(memo):
    ans += i * vv
    ans %= mod
print(ans)
