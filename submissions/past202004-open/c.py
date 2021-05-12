import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = [list(readline().rstrip().decode()) for _ in range(n)]
for i in range(n - 1, -1, -1):
    for j in range(2 * n - 1):
        if s[i][j] == '#':
            if i != n - 1:
                if s[i + 1][j] == 'X':
                    s[i][j] = 'X'
                if j != 0:
                    if s[i + 1][j - 1] == 'X':
                        s[i][j] = 'X'
                if j != 2 * (n - 1):
                    if s[i + 1][j + 1] == 'X':
                        s[i][j] = 'X'
for ss in s:
    print(*ss, sep='')
