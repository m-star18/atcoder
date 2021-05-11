import bisect
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
A = [0]*(n+1)
ans = 0
for i in range(n):
    A[i+1] = a[i]+A[i]
for i in range(n):
    s = bisect.bisect_left(A, k+A[i])
    ans += n+1-s
print(ans)
