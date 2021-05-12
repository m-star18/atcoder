import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def combination(n, r, mod=10 ** 9 + 7):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod


x, y = map(int, readline().split())
if (x + y) % 3 != 0 or not (x <= 2 * y and y <= 2 * x):
    print(0)
else:
    n = (x + y) // 3
    print(combination(n, y - n))
