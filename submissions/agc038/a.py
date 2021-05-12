import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w, a, b = map(int, read().split())
for i in range(b):
    print('1' * (w - a) + '0' * a)
for i in range(h - b):
    print('0' * (w - a) + '1' * a)
