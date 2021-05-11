import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
cnt = 0
for i in range(n):
    if a[a[i] - 1] == i + 1:
        cnt += 1
print(cnt // 2)
