a, b, k = map(int, input().split())
mx = max(a, b)
match, ans = 0, 0

for i in range(mx):
    if ((a % (mx - i)) == 0) and ((b % (mx - i)) == 0):
        
        match += 1
        ans = mx - i
        
        if match == k:
            break
print(ans)
