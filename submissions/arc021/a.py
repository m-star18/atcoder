import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = [list(map(int, readline().split())) for _ in range(4)]
for i in range(4):
    for j in range(3):
        if a[j][i] == a[j + 1][i] or a[i][j] == a[i][j + 1]:
            print('CONTINUE')
            exit()
print('GAMEOVER')
