import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, readline().split())
x = list(map(int, readline().split()))
ans = 0
for bf, af in zip(x, x[1:]):
    ans += min((af - bf) * a, b)
print(ans)
