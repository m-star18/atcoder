import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, readline().split())
if abs(a) == abs(b):
    print('Draw')
else:
    print('Ant' if abs(a) < abs(b) else 'Bug')
