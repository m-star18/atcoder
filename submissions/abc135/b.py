import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
p = list(map(int, input().split()))
for i in range(n):
    if i+1 != p[i]:
        cnt += 1
if cnt <= 2:
    ans = "YES"
else:
    ans = "NO"
print(ans)
