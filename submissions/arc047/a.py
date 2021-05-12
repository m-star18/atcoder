import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, l = map(int, readline().split())
s = readline().rstrip().decode()
cnt = 0
ans = 0
for ss in s:
    if ss == '+':
        cnt += 1
        if cnt == l:
            cnt = 0
            ans += 1
    else:
        cnt = max(0, cnt - 1)
print(ans)
