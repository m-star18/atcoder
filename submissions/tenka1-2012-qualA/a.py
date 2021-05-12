import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from functools import lru_cache


@lru_cache(maxsize=None)
def Fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)


n = int(readline())
print(Fib(n + 2))
