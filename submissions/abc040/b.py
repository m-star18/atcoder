import sys
input = sys.stdin.readline

n = int(input())
ans = 10**9
for i in range(1, n+1):
    for j in range(1+n):
        if i*j > n:
            break
        if ans > abs(i-j) + n-i*j:
            ans = abs(i-j) + n-i*j
print(ans)
