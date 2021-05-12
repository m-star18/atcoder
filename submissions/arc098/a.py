n = int(input())
s = list(input().rstrip('\n'))
cumsum = [[0, 0] for i in range(n)]
cnt_1 = 0
cnt_2 = 0
cnt = [-1] * n
for i in range(n):
    if s[i] == 'E':
        cnt_1 += 1
    else:
        cnt_2 += 1
    cumsum[i][0] = cnt_1
    cumsum[i][1] = cnt_2
for i in range(n):
    if s[i] == 'E':
        cnt[i] += 1
    cnt[i] += cumsum[n - 1][0] - cumsum[i][0] + cumsum[i][1]
print(min(cnt))
