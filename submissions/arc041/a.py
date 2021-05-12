import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x, y = map(int, readline().split())
k = int(readline())
if y >= k:
    print(x + k)
else:
    print(2 * y + x - k)
