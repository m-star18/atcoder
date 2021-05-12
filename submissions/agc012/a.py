import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = sorted(tuple(map(int, readline().split())), reverse=True)
cnt = 0
for i in range(n):
    cnt += a[i * 2 + 1]
print(cnt)
