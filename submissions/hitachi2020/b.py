import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, m = map(int, readline().split())
aa = list(map(int, readline().split()))
bb = list(map(int, readline().split()))
xyc = [list(map(int, readline().split())) for _ in range(m)]
ans = float('inf')
for x, y, c in xyc:
    ans = min(aa[x - 1] + bb[y - 1] - c, ans)
aa.sort()
bb.sort()
print(min(ans, aa[0] + bb[0]))
