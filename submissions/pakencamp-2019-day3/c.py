import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s_a = []
memo = []
cnt = 0
for i in range(n):
    a = list(map(int, input().split()))
    s_a.append(a)

for i in range(m - 1):
    for j in range(1, m):
        for k in range(n):
            cnt += max(s_a[k][i], s_a[k][j])
        memo.append(cnt)
        cnt = 0

print(max(memo))
