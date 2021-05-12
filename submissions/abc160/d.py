import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, x, y = map(int, read().split())
ans = [0] * n
for k in range(1, n):
    for i in range(k + 1, n + 1):
        ans[min(i - k, abs(y - i) + abs(x - k) + 1)] += 1
print('\n'.join(map(str, ans[1:])))
