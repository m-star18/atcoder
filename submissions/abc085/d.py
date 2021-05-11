import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, h = map(int, readline().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, readline().split())
max_a = max(a)
check = len([i for i in b if i > max_a])
b.sort(reverse=True)
for i in range(check):
    h -= b[i]
    if h <= 0:
        print(i + 1)
        exit()
if h % max_a == 0:
    print(h // max_a + check)
else:
    print(h // max_a + check + 1)
