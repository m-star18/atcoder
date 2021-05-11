import sys
input = sys.stdin.readline

n, k = map(int, input().split())
if k == 1:
    ans = 0
else:
    ans = n-k
print(ans)
