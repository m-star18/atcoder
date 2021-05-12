import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
cnt = 1
check = a[0]
for i in range(1, n):
    if check < a[i]:
        check = a[i]
        cnt += 1
print(cnt)
