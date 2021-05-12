import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = [list(map(lambda x: int(x) - 1, readline().split())) for _ in range(n)]
q = list(range(n))
for cnt in range(1, n ** 2):
    qq = set()
    for x in q:
        if a[a[x][0]][0] == x:
            qq.add(x)
            qq.add(a[x][0])
    if qq:
        q = []
        for x in qq:
            a[x].pop(0)
            if a[x]:
                q.append(x)
    else:
        print(-1)
        break
    if not q:
        print(cnt)
        break
