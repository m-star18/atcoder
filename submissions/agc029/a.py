import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = read().rstrip().decode()
cnt = 0
ans = 0
for i, ss in enumerate(s):
    if ss == 'W':
        ans += i - cnt
        cnt += 1
print(ans)
