import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
a_cnt = 0
b_cnt = 0

for i in range(n * m):
    if ans % 2 == 0:
        if a[a_cnt] + x <= b[b_cnt]:
            ans += 1
        else:
            b_cnt += 1

    else:
        if b[b_cnt] + y <= a[a_cnt]:
            ans += 1
        else:
            a_cnt += 1

    if a_cnt == n or b_cnt == m:
        break

if a_cnt == n:
    ans += 1

print(ans // 2)
