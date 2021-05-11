import sys
input = sys.stdin.readline

n = int(input())
if n%3 == 0:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
