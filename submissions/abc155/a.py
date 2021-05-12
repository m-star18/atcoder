import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, readline().split())
if (a == b and a != c) or (b == c and a != b) or (a == c and a != b):
    print('Yes')
else:
    print('No')
