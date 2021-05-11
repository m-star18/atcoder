import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = int(read())
v = 10 ** 9
x = (v - s % v) % v
print(0, 0, v, 1, x, (s + x) // v)
