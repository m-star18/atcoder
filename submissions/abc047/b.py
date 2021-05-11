import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

w, h, n = map(int, readline().split())
xya = [list(map(int, readline().split())) for i in range(n)]
ans = [[0, w], [0, h]]
for x, y, a in xya:
    if a == 1 and ans[0][0] < x:
        ans[0][0] = x
    elif a == 2 and ans[0][1] > x:
        ans[0][1] = x
    elif a == 3 and ans[1][0] < y:
        ans[1][0] = y
    elif a == 4 and ans[1][1] > y:
        ans[1][1] = y
if ans[0][0] > ans[0][1] or ans[1][0] > ans[1][1]:
    print(0)
else:
    print((ans[0][1] - ans[0][0]) * (ans[1][1] - ans[1][0]))
