import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

sx, sy, tx, ty = map(int, read().split())
x = (tx - sx)
y = (ty - sy)
print('U' * y + 'R' * x + 'D' * y + 'L' * (x + 1) + 'U' * (y + 1) + 'R' * (x + 1) + 'DR' + 'D' * (y + 1) + 'L' * (x + 1) + 'U')
