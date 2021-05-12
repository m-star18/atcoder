import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)


def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res


n, a, b = map(int, readline().split())
mod = 10 ** 9 + 7
print(((pow(2, n, mod) - 1) % mod - (combination(n, a) % mod + combination(n, b) % mod) % mod) % mod)
