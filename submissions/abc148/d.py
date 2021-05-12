import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
ans = 0
cnt = 1
for i in range(n):
    if a[i] == cnt:
        cnt += 1
    else:
        ans += 1
if ans == n:
    print(-1)
else:
    print(ans)
