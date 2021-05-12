import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from functools import lru_cache

t = int(readline())
for _ in range(t):
    n, a, b, c, d = map(int, readline().split())

    @lru_cache(None)
    def check(n):
        if n == 0:
            return 0
        if n == 1:
            return d
        res = n * d
        if n % 2 == 0:
            res = min(res, check(n // 2) + a)
        else:
            res = min(res, check(n // 2) + a + d, check(n // 2 + 1) + a + d)
        if n % 3 == 0:
            res = min(res, check(n // 3) + b)
        else:
            res = min(res, check(n // 3) + b + (n % 3) * d, check(n // 3 + 1) + b + (3 - n % 3) * d)
        if n % 5 == 0:
            res = min(res, check(n // 5) + c)
        else:
            res = min(res, check(n // 5) + c + (n % 5) * d, check(n // 5 + 1) + c + (5 - n % 5) * d)
        return res


    print(check(n))
