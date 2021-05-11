import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ab = [list(map(int, readline().split())) for _ in range(n)]
me = ab[0]
ans = 0
for i, (a, b) in enumerate(ab):
    if i == 0:
        continue
    me_cnt = (me[0] - 1) // b
    cpu_cnt = (a - 1) // me[1]
    if me_cnt < cpu_cnt:
        ans = i
        me = a, b
for i, (a, b) in enumerate(ab):
    if i == ans:
        continue
    me_cnt = (me[0] - 1) // b
    cpu_cnt = (a - 1) // me[1]
    if me_cnt <= cpu_cnt:
        print(-1)
        exit()
print(ans + 1)
