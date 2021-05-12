import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
print((h - 1) * w + (w - 1) * h)
