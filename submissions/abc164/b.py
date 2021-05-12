import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c, d = map(int, readline().split())
for i in range(10000):
    c -= b
    if c <= 0:
        print('Yes')
        break
    a -= d
    if a <= 0:
        print('No')
        break
