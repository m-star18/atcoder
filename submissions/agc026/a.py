import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
cnt = 0
for i in range(1, n):
    if a[i] == a[i - 1]:
        a[i] = 0
        cnt += 1
print(cnt)
