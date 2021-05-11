import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left

a, b, q = map(int, readline().split())
s = [int(readline()) for _ in range(a)]
t = [int(readline()) for _ in range(b)]
s.sort()
t.sort()
inf = float('inf')
for i in range(q):
    x = int(readline())
    ans = inf
    index_s = bisect_left(s, x)
    index_t = bisect_left(t, x)
    if index_s > 0 and index_t > 0:
        ans = min(ans, x - min(s[index_s - 1], t[index_t - 1]))
    if index_s < a and index_t < b:
        ans = min(ans, max(s[index_s], t[index_t]) - x)
    if index_s > 0 and index_t < b:
        ans = min(ans, min((x - s[index_s - 1]) * 2 + t[index_t] - x, x - s[index_s - 1] + (t[index_t] - x) * 2))
    if index_s < a and index_t > 0:
        ans = min(ans, min((s[index_s] - x) * 2 + x - t[index_t - 1], s[index_s] - x + (x - t[index_t - 1]) * 2))
    print(ans)
