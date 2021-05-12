import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, k = map(int, readline().split())
if a + b < k:
    print(0, 0)
elif a < k:
    print(0, b - (k - a))
else:
    print(a - k, b)
