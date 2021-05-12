import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline()) - 1
m = int(readline())
s = readline().rstrip().decode()
idx = 0
cnt = 0
ans = 0
if m < 3:
    print(0)
    exit()
for i in range(m):
    if s[idx: idx + 3] == 'IOI':
        cnt += 1
        idx += 1
    else:
        ans += max(0, cnt - n)
        cnt = 0
    idx += 1
    if idx >= m:
        break
print(ans + max(0, cnt - n))
