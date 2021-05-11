import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product

n = int(readline())
f = [list(map(int, readline().split())) for _ in range(n)]
p = [list(map(int, readline().split())) for _ in range(n)]
ans = -float('inf')
for bit in list(product([0, 1], repeat=10))[1:]:
    v = 0
    for ff, pp in zip(f, p):
        cnt = 0
        for i, check in enumerate(ff):
            if bit[i] == check == 1:
                cnt += 1
        v += pp[cnt]
    if ans < v:
        ans = v
print(ans)
