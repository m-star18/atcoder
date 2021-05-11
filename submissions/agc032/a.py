import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *b = map(int, read().split())
ans = [0] * n
idx = 0
for i in range(n):
    for j, bb in enumerate(b):
        if j + 1 == bb:
            ans[i] = bb
            idx = j
    if ans[i] == 0:
        print(-1)
        exit()
    b.pop(idx)
print('\n'.join(map(str, ans[::-1])))
