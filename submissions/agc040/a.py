import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
cnt = [[0, 0] for i in range(len(s) + 1)]
ans = 0
for i in range(len(s)):
    if s[i] == '<':
        cnt[i + 1][0] += 1
    else:
        cnt[i][1] += 1
for i in range(1, len(s) + 1):
    if cnt[i - 1][1] == 0:
        cnt[i][0] += cnt[i - 1][0]
    if cnt[len(s) - i + 1][0] == 0:
        cnt[len(s) - i][1] += cnt[len(s) - i + 1][1]
for i in range(len(s) + 1):
    ans += max(cnt[i])
print(ans)
