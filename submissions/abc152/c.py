import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
p = list(map(int, readline().split()))
cnt = 0
min_p = float('inf')
for i in range(n):
    min_p = min(min_p, p[i])
    if min_p == p[i]:
        cnt += 1
print(cnt)
