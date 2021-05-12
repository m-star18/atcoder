import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x, y, w = readline().rstrip().decode().split()
x, y = int(x) - 1, int(y) - 1
c = [readline().rstrip().decode() for _ in range(9)]
ans = c[y][x]
move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1), 'RU': (1, -1), 'RD': (1, 1), 'LU': (-1, -1), 'LD': (-1, 1)}
flag_x, flag_y = False, False
for i in range(3):
    dx, dy = move[w]
    if x + dx < 0 or x + dx > 8:
        flag_x = True
    if y + dy < 0 or y + dy > 8:
        flag_y = True

    if flag_x:
        x -= dx
    else:
        x += dx
    if flag_y:
        y -= dy
    else:
        y += dy
    ans += c[y][x]
print(ans)
