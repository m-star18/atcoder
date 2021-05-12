import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import accumulate

n, q = map(int, readline().split())
lr = [list(map(int, readline().split())) for _ in range(q)]
check = [0] * (n + 1)
for l, r in lr:
    check[l - 1] += 1
    check[r] -= 1
cumsum = list(accumulate(check))
print(''.join(map(lambda x: str(x % 2), cumsum[:-1])))
