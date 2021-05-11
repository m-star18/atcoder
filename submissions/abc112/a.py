import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
if n == 1:
    print('Hello World')
else:
    a, b = map(int, read().split())
    print(a + b)
