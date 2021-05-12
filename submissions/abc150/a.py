import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

k, x = map(int, readline().split())
if 500 * k >= x:
    print('Yes')
else:
    print('No')
