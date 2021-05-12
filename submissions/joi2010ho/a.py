import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import accumulate

n, m = map(int, readline().split())
s = [int(readline()) for _ in range(n - 1)]
cumsum = [0] + list(accumulate(s))
mod = 10 ** 5
ans = 0
left = 0
for _ in range(m):
    a = int(readline())
    ans += abs(cumsum[left + a] - cumsum[left])
    left += a
print(ans % mod)
