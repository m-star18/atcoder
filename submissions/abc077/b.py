import sys
input = sys.stdin.readline

n = int(input())
for i in range(max(n, 10**6)):
    if n < i**2:
        ans = (i-1)**2
        break
print(ans)
