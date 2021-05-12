import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m, d = map(int, read().split())
if d == 0:
    print((m - 1) / n)
else:
    print(2 * (n - d) * (m - 1) / (n ** 2))
