import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n < k:
    ans = n*x
else:
    ans = k*x + (n-k)*y
print(ans)
