import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from copy import deepcopy

h, w = map(int, readline().split())
s = [input() for _ in range(h)]
cnt_x = [[0] * w for _ in range(h)]
cnt_y = deepcopy(cnt_x)
for i in range(h):
    memo = 0
    for j in range(w):
        if s[i][j] == '.':
            memo += 1
            cnt_x[i][j] = memo
        else:
            memo = 0
    for j in range(w - 1, 0, -1):
        if s[i][j - 1] == '.':
            if cnt_x[i][j - 1] < cnt_x[i][j]:
                cnt_x[i][j - 1] = cnt_x[i][j]
for i in range(w):
    memo = 0
    for j in range(h):
        if s[j][i] == '.':
            memo += 1
            cnt_y[j][i] = memo
        else:
            memo = 0
    for j in range(h - 1, 0, -1):
        if s[j - 1][i] == '.':
            cnt_y[j - 1][i] = max(cnt_y[j - 1][i], cnt_y[j][i])
            if cnt_y[j - 1][i] < cnt_y[j][i]:
                cnt_y[j - 1][i] = cnt_y[j][i]
ans = 0
for i in range(h):
    for j in range(w):
        v = cnt_x[i][j] + cnt_y[i][j] - 1
        if ans < v:
            ans = v
print(ans)
