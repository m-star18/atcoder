import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

k, t, *a = map(int, read().split())
print(max(0, 2 * max(a) - k - 1))
