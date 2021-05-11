import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in range(n)]
dict = defaultdict(int)
dict[0] = 0
for i, check in enumerate(xy):
    for dxy in xy[i + 1:]:
        y, x = check[0], check[1]
        dy, dx = dxy[0], dxy[1]
        dict[(y - dy, x - dx)] += 1
        dict[(dy - y, dx - x)] += 1
print(n - max(dict.values()))
