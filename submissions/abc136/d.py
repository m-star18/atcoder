import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
cnt = 0
ans = [0] * len(s)
for i, ss in enumerate(s):
    if ss == 'L':
        ans[i] += cnt // 2
        ans[i - 1] += cnt // 2
        if cnt % 2 == 1:
            ans[i - 1] += 1
        cnt = 0
    else:
        cnt += 1
ans = ans[::-1]
for i, ss in enumerate(s[::-1]):
    if ss == 'R':
        ans[i] += cnt // 2
        ans[i - 1] += cnt // 2
        if cnt % 2 == 1:
            ans[i - 1] += 1
        cnt = 0
    else:
        cnt += 1
print(*ans[::-1])
