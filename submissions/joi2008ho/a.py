import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *c = map(int, read().split())
now = [[c[0], 1]]
for i, cc in enumerate(c[1:], 2):
    color, num = now[-1]
    if color == cc:
        now[-1][1] += 1
    else:
        if i & 1:
            now.append([cc, 1])
        else:
            now.pop()
            if now:
                now[-1][1] += num + 1
            else:
                now.append([cc, num + 1])
print(sum(cnt for color, cnt in now if not color))
