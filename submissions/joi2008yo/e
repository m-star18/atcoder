import sys
import itertools
input = sys.stdin.readline

r, c = map(int, input().split())
a_1 = []
a_2 = []
ans = [0] * (2 ** r)
bit = list(itertools.product([0, 1], repeat=r))

for i in range(r):
    a_i = list(map(int, input().split()))
    a_1.append(a_i)

for i in range(r):
    a_i = [0] * c
    for j in range(c):
        if a_1[i][j] == 0:
            a_i[j] = 1
        else:
            a_i[j] = 0
    a_2.append(a_i)

for i in range(2 ** r):
    check = []
    cnt = 0
    for j in range(r):
        if bit[i][j] == 1:
            check.append(a_2[j])
        else:
            check.append(a_1[j])

    for j in range(c):
        cnt_0 = 0
        cnt_1 = 0
        for k in range(r):
            if check[k][j] == 1:
                cnt_1 += 1
            else:
                cnt_0 += 1
        cnt += max(cnt_0, cnt_1)
    ans[i] = cnt

print(max(ans))
