n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

for i in range(n):
    h[i] = abs(t-h[i]*0.006-a)
ans = h.index(min(h))+1
print(ans)
