import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
h = [int(readline()) for _ in range(n)]
h.sort()
ans = float('inf')
for bf, af in zip(h, h[k - 1:]):
    ans = min(ans, af - bf)
print(ans)
