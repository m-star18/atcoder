import sys
input = sys.stdin.readline

n, d = map(int, input().split())
x = []
cnt = 0
ans = 0
for i in range(n):
    x_memo = list(map(int, input().split()))
    x.append(x_memo)

for i in range(n - 1):
    for j in range(i + 1, n):
        cnt = 0
        for k in range(d):
            cnt += abs(x[i][k] - x[j][k]) ** 2
        cnt = cnt ** 0.5
        if cnt.is_integer():
            ans += 1

print(ans)
