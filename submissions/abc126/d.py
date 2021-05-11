import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import heapq


def dijkstra_heap(s):
    # 始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n  # True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist, e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        # まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, [e[0] + d[v], e[1]])
    return d


n = int(readline())
edge = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, readline().split())
    if i == 0:
        s = [u, v]
    edge[u - 1].append([w, v - 1])
    edge[v - 1].append([w, u - 1])
d = dijkstra_heap(0)
for k in d:
    if k % 2 == 0:
        print('0')
    else:
        print('1')
