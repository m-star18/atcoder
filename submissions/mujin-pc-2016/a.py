import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

c = input()
right = ['O', 'P', 'K', 'L']
if c in right:
    print('Right')
else:
    print('Left')
