import sys
read = sys.stdin.buffer.read
readline = sys.stdin.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_right

n = int(readline())
s = [int(readline()) for i in range(n)]
a = sorted(s)
for check in s:
    print(n - bisect_right(a, check) + 1)
