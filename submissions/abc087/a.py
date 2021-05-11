import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x = int(readline())
a = int(readline())
b = int(readline())
print(max(0, (x - a) % b))
