import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
lr = [list(map(int, readline().split())) for i in range(n)]
for l, r in lr:
    n += r - l
print(n)
