import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

n, *a = map(int, read().split())
dict = defaultdict(int)
ans = 0
for i in range(n - 1, -1, -1):
    ans += dict[-a[i] - i]
    dict[a[i] - i] += 1
print(ans)
