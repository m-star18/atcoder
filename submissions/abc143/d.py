import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left

n = int(readline())
l = sorted(list(map(int, readline().split())))
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        ans += bisect_left(l, l[i] + l[j]) - (j + 1)
print(ans)
