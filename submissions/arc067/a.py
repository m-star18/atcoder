import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


n = int(readline())
check = []
for i in range(1, n + 1):
    check += prime_decomposition(i)
ans = 1
mod = 10 ** 9 + 7
for v in Counter(check).values():
    ans *= v + 1
    ans %= mod
print(ans)
