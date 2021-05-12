import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, c = map(int, readline().split())
s = input()
cnt_1 = 0
cnt_2 = n - 1
cnt = [0, 0]
ans = [0] * n
for i in range(n):
    if s[cnt_1] == 'o':
        ans[cnt_1] += 1
        cnt_1 += c
        cnt[0] += 1
    cnt_1 += 1
    if cnt_1 > n - 1:
        break
for i in range(n):
    if s[cnt_2] == 'o':
        ans[cnt_2] += 1
        cnt_2 -= c
        cnt[1] += 1
    cnt_2 -= 1
    if cnt_2 < 0:
        break
if max(cnt) > k:
    print()
else:
    for i in range(n):
        if ans[i] == 2:
            print(i + 1)
