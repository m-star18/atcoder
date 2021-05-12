import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n, *a = map(int, read().split())
counter = Counter(a).values()
ans = len(counter)
if (sum(counter) - ans) % 2 == 1:
    ans -= 1
print(ans)
