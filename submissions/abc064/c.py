import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = 0
rate_cnt = [0]*8
for i in range(n):
    if a[i] >= 3200:
        cnt += 1
    elif a[i] >= 2800:
        rate_cnt[7] += 1
    elif a[i] >= 2400:
        rate_cnt[6] += 1
    elif a[i] >= 2000:
        rate_cnt[5] += 1
    elif a[i] >= 1600:
        rate_cnt[4] += 1
    elif a[i] >= 1200:
        rate_cnt[3] += 1
    elif a[i] >= 800:
        rate_cnt[2] += 1
    elif a[i] >= 400:
        rate_cnt[1] += 1
    else:
        rate_cnt[0] += 1
for j in range(8):
    if 0 in rate_cnt:
        rate_cnt.remove(0)
    else:
        break
max_ans = len(rate_cnt)+cnt
if len(rate_cnt) == 0:
    min_ans = 1
else:
    min_ans = len(rate_cnt)
print(min_ans, max_ans)
