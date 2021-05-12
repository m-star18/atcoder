import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools
from math import sqrt

n = int(readline())
xy = [list(map(int, readline().split())) for i in range(n)]
memo = [i for i in range(n)]
z = list(itertools.permutations(memo))
ans = 0
for i in range(len(z)):
    for j in range(n - 1):
        ans += sqrt((xy[z[i][j]][0] - xy[z[i][j + 1]][0]) ** 2 + (xy[z[i][j]][1] - xy[z[i][j + 1]][1]) ** 2)
print(ans / len(z))
