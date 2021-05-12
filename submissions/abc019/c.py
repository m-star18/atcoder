import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
for i in range(n):
    while a[i] % 2 == 0:
        a[i] //= 2
print(len(set(a)))
