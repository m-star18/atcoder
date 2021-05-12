import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, x = map(int, readline().split())
ans = 0
for d in range(1, 20):
    c = (x - b * d) // a
    if c >= 0:
        ans = max(ans, min(c, 10 ** d - 1))
print(min(ans, 10 ** 9))
