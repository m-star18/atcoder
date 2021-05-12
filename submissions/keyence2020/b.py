import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
xl = [list(map(int, readline().split())) for i in range(n)]
pm = [[0] * 2 for _ in range(n)]
for i in range(n):
    pm[i][0] = xl[i][0] + xl[i][1]
    pm[i][1] = xl[i][0] - xl[i][1]
pm.sort()
ans = 1
check = pm[0][0]
for i in range(1, n):
    if check <= pm[i][1]:
        check = pm[i][0]
        ans += 1
print(ans)
