n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
code = 0

for i in range(n):
    a = list(map(int, input().split()))
    
    for j in range(m):
        code += a[j] * b[j]
    
    code += c
    if code > 0:
        ans += 1
    code = 0
        
print(ans)
