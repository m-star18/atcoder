import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, c, k = map(int, readline().split())
t = [int(readline()) for _ in range(n)]
t.sort()
ans = 1
tmp = [t[0], 0]
for tt in t:
    if tmp[0] + k < tt or tmp[1] + 1 > c:
        ans += 1
        tmp = [tt, 0]
    tmp[1] += 1
print(ans)
