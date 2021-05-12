import sys
import itertools
input = sys.stdin.readline

n = int(input())
t = [0] * n
bit = list(itertools.product([0, 1], repeat=n))
for i in range(n):
    t[i] = int(input())
ans = sum(t)

for i in range(2 ** n):
    cnt_1 = 0
    cnt_2 = 0

    for j in range(n):
        if bit[i][j] == 0:
            cnt_1 += t[j]
        else:
            cnt_2 += t[j]

    min_cnt = max(cnt_1, cnt_2)
    if min_cnt < ans:
        ans = min_cnt

print(ans)
