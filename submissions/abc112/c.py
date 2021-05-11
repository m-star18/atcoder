import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
xyh = [list(map(int, readline().split())) for _ in range(n)]
xyh.sort(key=lambda x: -x[2])
for dx in range(101):
    for dy in range(101):
        check = abs(xyh[0][0] - dx) + abs(xyh[0][1] - dy) + xyh[0][2]
        for x, y, h in xyh[1:]:
            if max(check - abs(x - dx) - abs(y - dy), 0) != h:
                break
        else:
            print(dx, dy, check)
            exit()
