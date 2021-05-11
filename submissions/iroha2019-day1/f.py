import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


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


n, k = map(int, read().split())
memo = prime_decomposition(n)
if len(memo) < k:
    print(-1)
else:
    for i in range(len(memo) - k):
        v = memo.pop(-1)
        memo[-1] *= v
    print(*memo)
