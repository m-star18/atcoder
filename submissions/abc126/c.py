import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, read().split())
ans = 0
for i in range(1, n + 1):
    cnt = 0
    while i < k:
        cnt += 1
        i *= 2
    ans += (1 / n) * pow(0.5, cnt)
print(ans)
