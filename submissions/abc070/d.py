import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import heapq


def dijkstra_heap(s, edge):
    # 始点sから各頂点への最短距離
    d = [10 ** 20] * n
    used = [True] * n  # True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a, b in edge[s]:
        heapq.heappush(edgelist, a * (10 ** 6) + b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        # まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge % (10 ** 6)]:
            continue
        v = minedge % (10 ** 6)
        d[v] = minedge // (10 ** 6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, (e[0] + d[v]) * (10 ** 6) + e[1])
    return d


n = int(readline())
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b, c = map(int, readline().split())
    edge[a - 1].append([c, b - 1])
    edge[b - 1].append([c, a - 1])
q, k = map(int, readline().split())
check = dijkstra_heap(k - 1, edge)
for i in range(q):
    x, y = map(int, readline().split())
    print(check[x - 1] + check[y - 1])
