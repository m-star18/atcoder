import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, read().split())
m -= 2 * n
if m < 0 or m > 2 * n:
    print(-1, -1, -1)
    exit()
q, r = divmod(m, 2)
print(n - q - r, r, q)
