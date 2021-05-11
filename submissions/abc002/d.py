import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product

n, m = map(int, readline().split())
xy = [list(map(int, readline().split())) for _ in range(m)]
graph = [[True] * n for _ in range(n)]
for x, y in xy:
    graph[x - 1][y - 1] = False
    graph[y - 1][x - 1] = False
ans = []
for bit in product([0, 1], repeat=n):
    flag = True
    for j in range(n):
        if bit[j] == 1:
            for k in range(n):
                if j == k:
                    continue
                if bit[k] == 1 and graph[j][k]:
                    flag = False
                    break
    if flag:
        ans.append(bit.count(1))
print(max(ans))
