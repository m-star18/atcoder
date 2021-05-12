import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import floor

a, b = map(int, readline().split())
for i in range(100000):
    if floor(i * 0.08) == a and floor(i * 0.1) == b:
        print(i)
        exit()
print(-1)
