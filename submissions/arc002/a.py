import sys
input = sys.stdin.readline

y = int(input())
if y%4 == 0:
    ans = 'YES'
    if y%100 == 0:
        ans = 'NO'
        if y%400 == 0:
            ans = 'YES'
else:
    ans = 'NO'
print(ans)
