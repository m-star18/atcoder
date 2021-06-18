import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
mod = 10 ** 9 + 7
ans = 0
x = 1
for bit in range(60):
    b = 0
    for i, aa in enumerate(a):
        if aa % 2:
            b += 1
        a[i] //= 2
    ans += (x * b * (n - b)) % mod
    ans %= mod
    x *= 2
    x %= mod
print(ans)
