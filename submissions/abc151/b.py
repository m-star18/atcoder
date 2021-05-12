import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, m = map(int, readline().split())
a = list(map(int, readline().split()))
sum_a = sum(a)
if sum(a) + k >= n * m:
    if sum(a) >= n * m:
        print(0)
        exit()
    print(n * m - sum(a))
else:
    print(-1)
