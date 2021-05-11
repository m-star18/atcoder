a, b, c = map(int, input().split())

if a+b < c:
    ans = 1+a+2*b
else:
    ans = 0
    if a <= c:
        ans += a+(c-a)*2+(b-c+a)
    elif a>= c:
        ans += c+b
    
print(ans)
