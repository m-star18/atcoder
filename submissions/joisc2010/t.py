import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

n, m, t, x, y = map(int, readline().split())
p = [int(readline()) for _ in range(m)]
check = [defaultdict(list) for _ in range(n)]
ans = [0] * n
for _ in range(y):
    t, n, m, flag = readline().rstrip().decode().split()
    t = int(t)
    n = int(n) - 1
    m = int(m) - 1
    if flag == 'open':
        check[n][m] = [t, 0]
    elif flag == 'incorrect':
        check[n][m][1] += 120
    else:
        ans[n] += max(x, p[m] - (t - check[n][m][0]) - check[n][m][1])
print('\n'.join(map(str, ans)))
