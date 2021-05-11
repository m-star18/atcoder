import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ab = [list(map(int, readline().split())) for _ in range(n)]
for a, b in ab:
    if a < b:
        a, b = b, a
    if a % b == 0:
        print(-1)
    else:
        print(a - b)
