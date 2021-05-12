import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, m, r = map(int, readline().split())
s = sorted([int(readline()) for _ in range(n - 1)], reverse=True)
if sum(s[:k]) / k >= r:
    print(0)
else:
    check = k * r - sum(s[:k - 1])
    if check <= m:
        print(check)
    else:
        print(-1)
