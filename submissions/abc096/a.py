a, b = map(int, input().split())
ab = a*100+b
ans = 0

for i in range(1, 13):
    if ab < 100*i+i:
        break
    ans += 1
print(ans)
