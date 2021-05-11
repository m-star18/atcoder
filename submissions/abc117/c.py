import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m, *x = map(int, read().split())
x.sort(reverse=True)
memo = [0] * m
for i, (bf, af) in enumerate(zip(x, x[1:])):
    memo[i] = bf - af
memo.sort(reverse=True)
print(sum(memo[n - 1:]))
