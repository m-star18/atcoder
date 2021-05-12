import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
h = list(map(int, readline().split()))
cnt = 0
ans = 0
for i in range(1, n):
    if h[i] > h[i - 1]:
        ans = max(ans, cnt)
        cnt = 0
    else:
        cnt += 1
print(max(ans, cnt))
