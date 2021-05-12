import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, n = map(int, readline().split())
a = list(map(int, readline().split()))
if sum(a) >= h:
    print('Yes')
else:
    print('No')
