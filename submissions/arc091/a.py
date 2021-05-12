import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
if n == 1 or m == 1:
    if n == 1 and m == 1:
        print(1)
    else:
        print(n * m - 2)
else:
    print(n * m - (n + m - 2) * 2)
