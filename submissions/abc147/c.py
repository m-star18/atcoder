import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n = int(readline())
s = [[] for i in range(n)]
u = [[] for j in range(n)]
for j in range(n):
    a = int(readline())
    for k in range(a):
        x, y = map(int, readline().split())
        if y == 1:
            s[j].append(x)
        else:
            u[j].append(x)
bit = list(itertools.product([0, 1], repeat=n))
ans = 0
for i in range(2 ** n):
    flag = True
    memo = []
    check_s = []
    check_u = []
    for j in range(n):
        if bit[i][j] == 1:
            memo.append(j + 1)
            check_s += s[j]
            check_u += u[j]
    if len(set(check_u) & set(memo)) == 0:
        for j in range(len(check_s)):
            if (check_s[j]) not in memo:
                flag = False
        if flag:
            ans = max(ans, len(memo))
print(ans)
