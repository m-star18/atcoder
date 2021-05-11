import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
ans = 0
l = list(range(n + 1))
r = list(range(n + 1))
memo = [0] * (n + 1)
for i, aa in enumerate(a):
    memo[aa] = i
for i in range(n, -1, -1):
    v = memo[i]
    ans += (v - l[v] + 1) * (r[v] - v + 1) * i
    l[r[v] + 1], r[l[v] - 1] = l[v], r[v]
print(ans)
