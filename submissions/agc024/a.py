import sys
input = sys.stdin.readline

a, b, c, k = map(int, input().split())
if k%2 == 0:
    ans = a-b
else:
    ans = b-a
if ans >= 10**18:
    ans = 'Unfair'
print(ans)
