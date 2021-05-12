import sys
input = sys.stdin.readline


def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)


def combination(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res


n = int(input())
k = int(input())
ans = combination(n + k - 1, k)
print(ans)
