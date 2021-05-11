a, b, t, = map(int, input().split())
ans = 0
t += 0.5

ans = int((t // a) * b)
print(ans)
