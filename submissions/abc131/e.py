import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
if k > (n - 1) * (n - 2) // 2:
    print(-1)
    exit()
m = n * (n - 1) // 2 - k
print(m)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        print(i, j)
        m -= 1
        if m == 0:
            exit()
