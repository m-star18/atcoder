import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def BellmanFord(edges, v, source):
    INF = float("inf")
    dist = [INF for _ in range(v)]
    dist[source] = 0
    for i in range(2 * v + 1):
        for now, fol, cost in edges:
            if dist[now] != INF and dist[fol] > dist[now] + cost:
                dist[fol] = dist[now] + cost
                if i >= v:
                    dist[fol] = -INF
    if dist[-1] == -INF:
        return -1
    else:
        return max(0, -dist[-1])


n, m, p = map(int, readline().split())
abc = [list(map(int, readline().split())) for i in range(m)]
edges = []
for a, b, c in abc:
    edges.append((a - 1, b - 1, p - c))
print(BellmanFord(edges, n, 0))
