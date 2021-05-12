import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
cnt = [[0, 0, 0]]
for i in range(n):
    s = readline().rstrip().decode()
    cnt.append([s.count('W'), s.count('B'), s.count('R')])
for i in range(n):
    for j in range(3):
        cnt[i + 1][j] += cnt[i][j]
ans = n * m
for i in range(1, n - 1):
    for j in range(i + 1, n):
        ans = min(ans, n * m - cnt[i][0] - (cnt[j][1] - cnt[i][1]) - (cnt[n][2] - cnt[j][2]))
print(ans)
