import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, read().split())
x, y = 0, 0
for i in range(1, n + 1):
    if i % k == 0:
        x += 1
    elif i * 2 % k == 0:
        y += 1
print(x ** 3 + y ** 3)
