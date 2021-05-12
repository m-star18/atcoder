import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
check = [0] * n
for i in range(n):
    check[i] = a[i] - b[i]
check.sort()
m_check = sorted(check, reverse=True)
m_cnt = 0
p = 0
ans = 0
for i in range(n):
    if check[i] < 0:
        p += check[i]
        ans += 1
    else:
        if p >= 0:
            print(ans)
            exit()
        else:
            p += m_check[m_cnt]
            m_cnt += 1
            ans += 1
if p >= 0:
    print(ans)
else:
    print(-1)
