import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(m)]
cnt = [0]
for a, b in ab:
    if a < b:
        cnt.append(n - a)
print(sum(cnt) - max(cnt))
