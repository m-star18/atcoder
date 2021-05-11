import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ab = [list(map(int, readline().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1])
cnt = 0
for a, b in ab:
    cnt += a
    if cnt > b:
        print('No')
        break
else:
    print('Yes')
