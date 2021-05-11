import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
v = list(map(int, readline().split()))
ans = -float('inf')
nk = min(n, k)
for a in range(nk + 1):
    for b in range(nk - a + 1):
        vv = v[:a] + v[n - b:]
        if k - a - b >= 0:
            vv.sort()
            cnt = 0
            for check in vv[:k - a - b]:
                if check >= 0:
                    break
                cnt += check
            ans = max(ans, sum(vv) - cnt)
print(ans)
