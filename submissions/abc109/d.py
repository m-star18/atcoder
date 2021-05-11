import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in range(h)]
cnt = 0
bf = []
af = []
for i in range(h):
    for j in range(w):
        if a[i][j] % 2 == 1:
            cnt += 1
            bf.append([i + 1, j + 1])
            if j == w - 1:
                if i == h - 1:
                    cnt -= 1
                    break
                a[i + 1][j] += 1
                af.append([i + 2, j + 1])
            else:
                a[i][j + 1] += 1
                af.append([i + 1, j + 2])
print(cnt)
for xy1, xy2 in zip(bf, af):
    print(*(xy1 + xy2))
