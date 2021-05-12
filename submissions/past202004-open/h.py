import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, m = map(int, input().split())
a = [[0 if aa == "S" else -1 if aa == "G" else int(aa) for aa in input()] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            s = i * m + j
        if a[i][j] == -1:
            g = i * m + j
move = ((0, 1), (0, -1), (1, 0), (-1, 0))


def check(s):
    q = deque([s])
    dict = [-1] * (10 * n * m)
    dict[s] = 0
    while q:
        x = q.popleft()
        t, i, j = x // (n * m), x // m % n, x % m
        for di, dj in move:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if a[ni][nj] != t + 1:
                    y = t * n * m + ni * m + nj
                else:
                    y = (t + 1) * n * m + ni * m + nj
                if dict[y] == -1:
                    dict[y] = dict[x] + 1
                    q.append(y)
    return dict


ans = check(s)
print(ans[9 * n * m + g])
