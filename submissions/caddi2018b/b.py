import sys
input = sys.stdin.readline

n, h, w = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    if ab[i][0] >= h and ab[i][1] >= w:
        ans += 1
print(ans)
