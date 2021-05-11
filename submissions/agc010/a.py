import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i]%2 == 1:
        cnt += 1
if cnt%2 == 0:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
