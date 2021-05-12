import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
s = [readline().rstrip().decode() for _ in range(h)]
for i in range(h):
    ans = [-1] * w
    flag = False
    cnt = 0
    for j in range(w):
        if s[i][j] == 'c':
            ans[j] = 0
            cnt = 1
            flag = True
        elif flag:
            ans[j] = cnt
            cnt += 1
    print(*ans)
