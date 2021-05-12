import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from copy import deepcopy

a = ['x' * 12] + ['x' + readline().rstrip().decode() + 'x' for i in range(10)] + ['x' * 12]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 1
for i in range(1, 11):
    for j in range(1, 11):
        if a[i][j] == 'o':
            cnt += 1

memo = [[False] * 12 for _ in range(12)]
for i in range(1, 11):
    for j in range(1, 11):
        check = deepcopy(memo)
        q = [(i, j)]
        ans = 0
        while q:
            y, x = q.pop()
            ans += 1
            for dy, dx in move:
                xx = x + dx
                yy = y + dy
                if check[yy][xx] or a[yy][xx] == 'x':
                    continue
                q.append((yy, xx))
                check[yy][xx] = True
        if ans == cnt:
            print('YES')
            exit()
print('NO')
