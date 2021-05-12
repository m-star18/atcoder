import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s, l, r = map(int, readline().split())
if l > s:
    print(l)
elif r < s:
    print(r)
else:
    print(s)
