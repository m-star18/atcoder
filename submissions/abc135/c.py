import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] <= 0:
        a[i] = 0
    if b[i] > a[i]:
        check = a[i+1]+a[i]
        a[i+1] -= b[i]-a[i]
    else:
        a[i] -= b[i]
    if a[i+1] <= 0:
        cnt += check
    else:
        cnt += b[i]
print(cnt)
