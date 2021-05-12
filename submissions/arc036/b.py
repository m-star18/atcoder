import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
h = [int(readline()) for _ in range(n)]
memo = [0]
for i in range(1, n - 1):
    if h[i - 1] > h[i] < h[i + 1]:
        memo.append(i)
memo.append(n - 1)
ans = 0
for i in range(len(memo) - 1):
    ans = max(ans, memo[i + 1] - memo[i] + 1)
print(ans)
