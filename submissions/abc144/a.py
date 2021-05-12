import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, readline().split())
if a > 9 or b > 9:
    print(-1)
else:
    print(a * b)
