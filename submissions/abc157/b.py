import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = [list(map(int, readline().split())) for i in range(3)]
n = int(readline())
b = [int(readline()) for _ in range(n)]
for bb in b:
    for j in range(3):
        for k in range(3):
            if a[j][k] == bb:
                a[j][k] = 0
ans = 'No'
for i in range(3):
    if a[i][0] == a[i][1] == a[i][2] == 0:
        ans = 'Yes'
    if a[0][i] == a[1][i] == a[2][i] == 0:
        ans = 'Yes'
if a[0][0] == a[1][1] == a[2][2] == 0:
    ans = 'Yes'
if a[2][0] == a[1][1] == a[0][2] == 0:
    ans = 'Yes'
print(ans)
