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


n, p = map(int, read().split())
ans = 1
for k, v in Counter(prime_decomposition(p)).items():
    v //= n
    ans *= k ** v
print(ans)
