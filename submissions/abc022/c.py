def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import floyd_warshall

    n, m = map(int, readline().split())
    inf = float('inf')
    graph = [[inf] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v, l = map(int, readline().split())
        graph[u][v] = l
        graph[v][u] = l
    memo = []
    for i in range(1, n):
        graph[i][i] = 0
        if graph[1][i] != inf:
            memo.append((i, graph[1][i]))
        graph[1][i] = inf
    cost = floyd_warshall(csr_matrix(graph))
    ans = inf
    for idx, (i1, i2) in enumerate(memo):
        for j1, j2 in memo[idx + 1:]:
            ans = min(ans, i2 + j2 + cost[i1][j1])
    print(int(ans) if ans != inf else -1)


if __name__ == '__main__':
    main()
