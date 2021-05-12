def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from collections import deque

    h, w, k = map(int, readline().split())
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, readline().split())
    dict = [[-1] * w for _ in range(h)]
    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for i in range(h):
        c = readline().rstrip().decode()
        for j, cc in enumerate(c):
            if cc == '@':
                dict[i][j] = 0
    q = deque()
    q.append((x1, y1))
    dict[x1][y1] = 0
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            exit(print(dict[x][y]))
        for dx, dy in move:
            for i in range(1, k + 1):
                xx = x + dx * i
                yy = y + dy * i
                if 0 > xx or xx >= h or 0 > yy or yy >= w:
                    break
                if 0 <= dict[xx][yy] <= dict[x][y]:
                    break
                if dict[xx][yy] == -1:
                    q.append((xx, yy))
                dict[xx][yy] = dict[x][y] + 1
    print(-1)


if __name__ == '__main__':
    main()
