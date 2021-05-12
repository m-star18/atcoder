import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import combinations_with_replacement

n, m, q = map(int, readline().split())
abcd = [list(map(int, readline().split())) for _ in range(q)]
ans = 0
for seq in combinations_with_replacement(range(m), n):
    cnt = 0
    for a, b, c, d in abcd:
        if seq[b - 1] - seq[a - 1] == c:
            cnt += d
    ans = max(ans, cnt)
print(ans)
