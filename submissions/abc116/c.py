import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *h = map(int, read().split())
ans = h[0]
for bf, af in zip(h, h[1:]):
    if af > bf:
        ans += af - bf
print(ans)
