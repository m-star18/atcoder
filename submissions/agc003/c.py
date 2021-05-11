import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left

n, *a = map(int, read().split())
b = sorted(a)
cnt = 0
for i, aa in enumerate(a):
    if abs(i - bisect_left(b, aa)) % 2 == 1:
        cnt += 1
print(cnt // 2)
