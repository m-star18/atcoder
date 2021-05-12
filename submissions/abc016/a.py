import sys
input = sys.stdin.readline

m, d = map(int, input().split())

if m % d == 0:
    ans = 'YES'
else:
    ans = 'NO'
   
print(ans)
