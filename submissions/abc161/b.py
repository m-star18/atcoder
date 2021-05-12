import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
sum_a = sum(a)
cnt = 0
for i in range(n):
    if a[i] / sum_a >= 1 / (4 * m):
        cnt += 1
if cnt >= m:
    print('Yes')
else:
    print('No')
