import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque


def bfs(s, flag):
    if flag:
        global check
    else:
        check = [-1] * (n + 1)
    cnt = 0
    ans = 0
    q = deque([s, cnt])
    while q:
        now = q.popleft()
        cnt = q.popleft()
        check[now] = cnt
        ans += 1
        for next in graph[now]:
            if flag:
                if check[next] > cnt + 1:
                    q.append(next)
                    q.append(cnt + 1)
            else:
                if check[next] == -1:
                    q.append(next)
                    q.append(cnt + 1)
    if flag:
        return ans
    else:
        return check


n = int(readline())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)
check = bfs(1, False)
print('Snuke' if bfs(n, True) >= n / 2 else 'Fennec')
