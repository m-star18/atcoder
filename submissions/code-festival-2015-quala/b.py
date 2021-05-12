import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
ans = a[0]
for i in range(1, n):
    ans = a[i] + ans * 2
print(ans)
