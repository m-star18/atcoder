import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
check = [0] * (n + 1)
for i in range(m):
    a, b = map(int, readline().split())
    check[a] += 1
    check[b] += 1
for v in check:
    if v % 2 == 1:
        print('NO')
        break
else:
    print('YES')
