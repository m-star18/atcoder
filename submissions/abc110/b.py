n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
maxs = max(x)
mins = min(y)

if X < max(x) and Y >= min(y) and max(x) < min(y):
    ans = 'No War'
else:
    ans = 'War'
print(ans)
