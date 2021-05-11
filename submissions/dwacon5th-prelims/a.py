import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
average = sum(a) / n
for i in range(n):
    a[i] -= average
    a[i] = abs(a[i])
check = min(a)
ans = a.index(check)
print(ans)
