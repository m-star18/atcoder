import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in range(n)]
ab.sort()
for a, b in ab:
    k -= b
    if k <= 0:
        print(a)
        break
