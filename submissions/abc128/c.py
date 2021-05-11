import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product

n, m = map(int, readline().split())
ks = [list(map(int, readline().split()))[1:] for _ in range(m)]
p = list(map(int, readline().split()))
ans = 0
for bit in product([0, 1], repeat=n):
    for pp, ksi in zip(p, ks):
        cnt = 0
        for j in range(n):
            if bit[j] == 1 and (j + 1) in ksi:
                cnt += 1
        if cnt % 2 != pp:
            break
    else:
        ans += 1

print(ans)
