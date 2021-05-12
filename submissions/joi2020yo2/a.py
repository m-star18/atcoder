import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

n = int(readline())
s = np.array([list(readline().rstrip().decode()) for _ in range(n)])
t = [readline().rstrip().decode() for _ in range(n)]
ans = float('inf')
for i in range(4):
    check = np.rot90(s, i)
    cnt = min(4 - i, i)
    for j in range(n):
        for k in range(n):
            if check[j][k] != t[j][k]:
                cnt += 1
    if ans > cnt:
        ans = cnt
print(ans)
