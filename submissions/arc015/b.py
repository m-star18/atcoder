import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * 6
for i in range(n):
    max, min = map(float, input().split())
    if max >= 35.0:
        ans[0] += 1
    elif 35.0 > max >= 30.0:
        ans[1] += 1
    elif 30.0 > max >= 25.0:
        ans[2] += 1
    if min >= 25.0:
        ans[3] += 1
    if min < 0 and max >= 0:
        ans[4] += 1
    elif max < 0:
        ans[5] += 1
print(*ans)
