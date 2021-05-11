import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n, k, *a = map(int, read().split())
counter = sorted(Counter(a).values())
ans = 0
for i in range(len(counter) - k):
    ans += counter[i]
print(ans)
