def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from collections import deque

    h, w = map(int, readline().split())
    size = [[0] * w for _ in range(h)]
    c = [readline().rstrip().decode() for _ in range(h)]
    dist = [[-1] * w for _ in range(h)]
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i, cc in enumerate(c):
        for j, ccc in enumerate(cc):
            if ccc == '.':
                continue
            if ccc == '#':
                size[i][j] = 1
            elif ccc == 's':
                q = deque([(i, j)])
                dist[i][j] = 0
            else:
                g = (i, j)
    while q:
        y, x = q.popleft()
        for dy, dx in move:
            xx = x + dx
            yy = y + dy
            if xx < 0 or yy < 0 or yy > h - 1 or xx > w - 1:
                continue
            if dist[yy][xx] != -1:
                continue
            dist[yy][xx] = dist[y][x]
            if size[yy][xx] == 1:
                dist[yy][xx] += size[yy][xx]
                q.append((yy, xx))
            else:
                dist[yy][xx] = dist[y][x]
                q.appendleft((yy, xx))
            if (yy, xx) == g:
                print('YES' if dist[yy][xx] <= 2 else 'NO')
                exit()


if __name__ == '__main__':
    main()
