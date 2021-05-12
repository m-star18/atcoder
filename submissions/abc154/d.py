import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
p = list(map(int, readline().split()))
cumsum = [0] * (n + 1)
for i in range(1, n + 1):
    cumsum[i] += cumsum[i - 1] + ((p[i - 1] * (p[i - 1] + 1)) // 2) / p[i - 1]
ans = [0] * (n - k + 1)
for i in range(n - k + 1):
    ans[i] = cumsum[i + k] - cumsum[i]
print(max(ans))
