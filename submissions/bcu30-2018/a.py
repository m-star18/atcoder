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
a = list(map(int, readline().split()))
m = int(readline())
b = list(map(int, readline().split()))
counter_a = []
counter_b = []
for aa in a:
    counter_a += prime_decomposition(aa)
for bb in b:
    counter_b += prime_decomposition(bb)
counter_a = sorted(list(Counter(counter_a).items()))
counter_b = sorted(list(Counter(counter_b).items()))
if set(counter_a) & set(counter_b) == set(counter_a):
    print('Yes')
else:
    print('No')
