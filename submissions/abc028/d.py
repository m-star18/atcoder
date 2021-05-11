import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, read().split())
ans = 1
if n > 1:
    ans += (n - 1) * 3 + (k - 1) * (n - k) * 6
print(ans / n ** 3)
