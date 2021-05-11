import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
xy = [list(map(int, readline().split())) for _ in range(m)]
flag = [False] * n
flag[0] = True
cnt = [1] * n
for x, y in xy:
    if flag[x - 1]:
        flag[y - 1] = True
    cnt[x - 1] -= 1
    cnt[y - 1] += 1
    if cnt[x - 1] == 0:
        flag[x - 1] = False
print(flag.count(True))
