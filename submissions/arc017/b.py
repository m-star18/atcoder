import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
a = [int(readline()) for _ in range(n)]
cnt = 1
ans = 0
for i in range(n - 1):
    if a[i] < a[i + 1]:
        cnt += 1
        if cnt >= k:
            ans += 1
    else:
        cnt = 1
if k == 1:
    ans = n
print(ans)
