import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
m = int(readline())
ab = [list(map(int, readline().split())) for _ in range(m)]
for a, b in ab:
    print(min(a - 1, n - a, b - 1, n - b) % 3 + 1)
