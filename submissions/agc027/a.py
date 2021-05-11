import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0
for i in range(n):
    x -= a[i]
    cnt += 1
    if x < 0:
        cnt -= 1
        break
if x > 0:
    cnt -= 1
print(cnt)
