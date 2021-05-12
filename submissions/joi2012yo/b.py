import sys
read = sys.stdin.buffer.read
readline = sys.stdin.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
cnt = [0] * n
for _ in range(n * (n - 1) // 2):
    a, b, c, d = map(int, readline().split())
    if c > d:
        cnt[a - 1] += 3
    elif c == d:
        cnt[a - 1] += 1
        cnt[b - 1] += 1
    else:
        cnt[b - 1] += 3
ans = sorted(cnt, reverse=True)
for i in range(n):
    print(ans.index(cnt[i]) + 1)
