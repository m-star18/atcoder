a, b = map(int, input().split())
c = [0]
for i in range(1, 1000):
    c.append(c[i-1]+i)
    if c[i-1]-a > 0:
        ans = c[i-1]-a
        if a+ans == c[i-1] and b+ans == c[i]:
            break
        else:
            ans = 0
print(ans)
