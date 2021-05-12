import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

p = min([int(readline()) for _ in range(3)])
g = min([int(readline()) for _ in range(2)])
print(p + g - 50)
