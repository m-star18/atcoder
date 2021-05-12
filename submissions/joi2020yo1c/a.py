import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x, l, r = map(int, readline().split())
if x < l:
    print(l)
elif l <= x <= r:
    print(x)
else:
    print(r)
