import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *p = map(int, read().split())
p += [0]
cnt = 0
for i, pp in enumerate(p):
    if (i + 1) == pp:
        p[i + 1] = 0
        cnt += 1
print(cnt)
