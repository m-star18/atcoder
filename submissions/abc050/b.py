import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for i in range(m)]
ans = sum(t)
for i in range(m):
    print(ans + px[i][1] - t[px[i][0] - 1])
