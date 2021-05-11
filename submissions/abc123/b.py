a = [int(input()) for i in range(5)]
n = 0
ans = 0

for x in a:
    if x % 10 != 0:
        t = 10 - x % 10
    else:
        t = 0
        
    ans += x + t
    n = max(n, t)
    
print(ans - n)
