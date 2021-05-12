import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, readline().split())
a = (a - 1) // 4 - (a - 1) // 100 + (a - 1) // 400
b = b // 4 - b // 100 + b // 400
print(b - a)
