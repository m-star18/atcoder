import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
h = [0] + list(map(int, readline().split()))
ab = [list(map(int, readline().split())) for _ in range(m)]
check = [True] * (n + 1)
for a, b in ab:
    if h[a] > h[b]:
        check[b] = False
    elif h[a] < h[b]:
        check[a] = False
    else:
        check[a] = False
        check[b] = False
print(check.count(True) - 1)
