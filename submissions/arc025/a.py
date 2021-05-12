import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

d = list(map(int, readline().split()))
j = list(map(int, readline().split()))
print(sum(max(dd, jj) for dd, jj in zip(d, j)))
