import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, *a = map(int, read().split())
v = 0
ans = 0
for i in range(40, -1, -1):
    cnt = 0
    for aa in a:
        if (aa >> i) & 1:
            cnt += 1
    if n - cnt > cnt and v + (1 << i) <= k:
        v += 1 << i
        ans += (n - cnt) * (1 << i)
    else:
        ans += cnt * (1 << i)
print(ans)
