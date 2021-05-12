def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from collections import deque, defaultdict

    n, m = map(int, readline().split())
    graph = [defaultdict(set) for _ in range(n + 1)]
    for _ in range(m):
        p, q, c = map(int, readline().split())
        graph[p][c].add(q)
        graph[q][c].add(p)
    q = deque([(1, 0, -1)])
    vis = set()
    while q:
        now, v, c = q.popleft()
        if now == n:
            print(v)
            exit()
        if (now, c) in vis:
            continue
        vis.add((now, c))
        if c == 0:
            for cc in graph[now]:
                for next in graph[now][cc]:
                    if (next, cc) not in vis:
                        q.append((next, v + 1, cc))
        else:
            for next in graph[now][c]:
                if (next, c) not in vis:
                    q.appendleft((next, v, c))
            if (now, 0) not in vis:
                q.appendleft((now, v, 0))
    print(-1)


if __name__ == '__main__':
    main()
