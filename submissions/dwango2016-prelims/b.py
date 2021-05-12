import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
k = list(map(int, readline().split()))
ans = [0] * n
ans[0] = k[0]
ans[-1] = k[-1]
for i in range(n - 2):
    if k[i] < k[i + 1]:
        ans[i + 1] = k[i]
    else:
        ans[i + 1] = k[i + 1]
print(*ans)
