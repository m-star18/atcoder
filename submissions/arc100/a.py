import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
a = sorted(aa - i for i, aa in enumerate(a))
print(sum(a[n // 2:]) - sum(a[:(n + 1) // 2]))
