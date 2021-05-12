import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, readline().split())
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in range(n)]
move = [(1, 0), (0, 1)]
q = [(1, 1)]
cnt = 0
while q:
    x, y = q.pop()
    for dx, dy in move:
        xx = x + dx
        yy = y + dy
        if (xx, yy) in xy or xx > a or yy > b:
            continue
        if xx == a and yy == b:
            cnt += 1
        else:
            q.append((xx, yy))
print(cnt)
