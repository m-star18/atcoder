import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = tuple(map(int, readline().split()))
cnt = 0
for i in range(n):
    if a[i] % 2 == 0:
        cnt += 1
print(3 ** n - 2 ** cnt)
