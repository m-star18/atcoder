import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s, w = map(int, read().split())
if w >= s:
    print('unsafe')
else:
    print('safe')
