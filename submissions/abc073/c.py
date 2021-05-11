import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(readline())
a = [int(readline()) for _ in range(n)]
ans = 0
for v in Counter(a).values():
    ans += 1 if v % 2 == 1 else 0
print(ans)
