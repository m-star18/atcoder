import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
h = sorted(list(map(int, readline().split())))
if n <= k:
    print(0)
else:
    print(sum(h[:n - k]))
