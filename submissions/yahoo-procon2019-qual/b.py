import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

a1, b1 = map(int, readline().split())
a2, b2 = map(int, readline().split())
a3, b3 = map(int, readline().split())
counter = sorted(list(Counter([a1, a2, a3, b1, b2, b3]).values()))
if counter == [1, 1, 2, 2]:
    print('YES')
else:
    print('NO')
