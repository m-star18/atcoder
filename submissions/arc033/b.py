import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = set(map(int, readline().split()))
b = set(map(int, readline().split()))
print(len(a & b) / len(a | b))
