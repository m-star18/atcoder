N = int(input())
x = [0] * N
u = [0] * N
ans = 0

for i in range(N):
    x[i], u[i] = map(str, input().split())
    x[i] = float(x[i])

    if u[i] == 'BTC':
        ans += x[i] * 380000
    else:
        ans += x[i]

print(ans)
