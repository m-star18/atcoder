import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
if b-a == c-b:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
