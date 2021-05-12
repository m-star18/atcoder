import sys
input = sys.stdin.readline

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(1, n + 1):
    if ab[n - i][0] != 0:
        ab[n - i][0] += cnt
        if ab[n - i][0] <= ab[n - i][1]:
            cnt += ab[n - i][1] - ab[n - i][0]
        else:
            if ab[n - i][0] % ab[n - i][1] != 0:
                cnt += ab[n - i][1] - (ab[n - i][0] % ab[n - i][1])
print(cnt)
