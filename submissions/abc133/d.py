import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(lambda x: int(x)*2, readline().split()))
ans = [0] * n
for i in range(n):
    if i % 2 == 0:
        ans[0] += a[i]
    else:
        ans[0] -= a[i]
ans[0] //= 2
for i in range(1, n):
    ans[i] = a[i - 1] - ans[i - 1]
print(*ans)
