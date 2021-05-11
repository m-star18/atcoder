n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0

for i in range(n):
    xy = v[i] - c[i]
    if xy > 0:
        ans += xy
        
print(ans)
