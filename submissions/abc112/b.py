N, T = map(int, input().split())
ans_c, ans = 1000, 0
for _ in range(N):
    c, t = map(int, input().split())
    
    if t <= T:
        ans += 1
        if ans_c >= c:
            ans_c = c
if ans != 0:
    ans = ans_c
else:
    ans = 'TLE'
print(ans)
