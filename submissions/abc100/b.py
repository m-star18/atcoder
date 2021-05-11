d, n = map(int, input().split())
for i in range(3):
    if d == i:
        if n == 100:
            ans = 101*100**d
        else:
            ans = n*100**d
print(ans)
