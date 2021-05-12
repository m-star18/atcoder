import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m, q = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, readline().split())
    graph[u].append(v)
    graph[v].append(u)
c = [0] + list(map(int, readline().split()))
for _ in range(q):
    s = readline().rstrip().decode()
    if s[0] == '1':
        _, x = s.split()
        x = int(x)
        print(c[x])
        for dx in graph[x]:
            c[dx] = c[x]
    else:
        _, x, y = s.split()
        x = int(x)
        print(c[x])
        c[x] = int(y)
