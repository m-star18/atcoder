import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, read().split())
if n % 2 == 1:
    for i in range(1, m + 1):
        print(i, n - i)
else:
    x, y = 0, 0
    for i in range(m):
        a, b = 2 * i, n - 2 * (i + 1)
        if a == b or (a == y and b == x):
            n -= 1
        x, y = a, b
        print(i + 1, n - i)
