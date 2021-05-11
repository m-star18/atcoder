import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ka = []
ans = 0
for i in range(n):
    ka_memo = list(map(int, input().split()))
    ka.append(ka_memo[1:])

for i in range(1, m + 1):
    flg = True
    for j in range(n):
        if i not in ka[j]:
            flg = False
            break
    if flg:
        ans += 1
print(ans)
