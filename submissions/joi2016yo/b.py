import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = [int(readline()) for _ in range(n)]
for k in range(1, m + 1):
    for i in range(n - 1):
        if a[i] % k > a[i + 1] % k:
            a[i], a[i + 1] = a[i + 1], a[i]
print('\n'.join(map(str, a)))
