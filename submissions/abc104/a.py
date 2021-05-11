r = int(input())

if r < 2800:
    if r < 1200:
        ans = 'ABC'
    else:
        ans = 'ARC'
else:
    ans = 'AGC'
print(ans)
