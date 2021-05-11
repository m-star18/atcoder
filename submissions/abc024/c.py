import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, d, k = map(int, readline().split())
lr = [list(map(int, readline().split())) for i in range(d)]
for i in range(k):
    s, t = map(int, readline().split())
    min_s = float('inf')
    max_t = 0
    cnt = 0
    for l, r in lr:
        cnt += 1
        if l <= s <= r or min_s <= l <= max_t or min_s <= r <= max_t:
            min_s = min(min_s, l)
            max_t = max(max_t, r)
        if min_s <= t <= max_t:
            print(cnt)
            break
