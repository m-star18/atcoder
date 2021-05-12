import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def bfs(s):
    from collections import deque
    check = [0] * (n + 1)
    check[s] = 1
    q = deque([s])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if check[next] == 0:
                check[next] = str(now)
                q.append(next)
    return check


n, m = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)
print('Yes')
print('\n'.join(bfs(1)[2:]))
