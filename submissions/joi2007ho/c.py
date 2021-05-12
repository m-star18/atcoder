import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
h = [tuple(map(int, readline().split())) for _ in range(n)]
check = set(h)
ans = 0
memo = 0
for x_1, y_1 in h:
    memo += 1
    for x_2, y_2 in h[memo:]:
        dx = x_2 - x_1
        dy = y_2 - y_1
        if (x_1 + dy, y_1 - dx) in check and (x_2 + dy, y_2 - dx) in check:
            ans = max(ans, dx ** 2 + dy ** 2)
print(ans)
