import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
a = [int(readline()) for _ in range(n)]
cnt = sum(a[0:k])
ans = max(sum(a[-k:]), cnt)
for i in range(k, n - 1):
    cnt += a[i] - a[i - k]
    if ans < cnt:
        ans = cnt
print(ans)
