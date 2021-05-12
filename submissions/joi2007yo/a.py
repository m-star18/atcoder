import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
print(max(sum(a), sum(b)))
