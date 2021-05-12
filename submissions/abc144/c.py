import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ans = float('inf')
for i in range(1, int(n ** 0.5) + 1):
    x, y = divmod(n, i)
    if y == 0:
        ans = min(ans, x + i)
print(ans - 2)
