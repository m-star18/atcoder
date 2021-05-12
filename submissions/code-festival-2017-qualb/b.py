import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(readline())
d = list(map(int, readline().split()))
m, *t = map(int, read().split())
d = Counter(d)
for k, v in Counter(t).items():
    if d[k] < v:
        print('NO')
        break
else:
    print('YES')
