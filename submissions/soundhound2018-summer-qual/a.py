import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, readline().split())
if a + b == 15:
    print('+')
elif a * b == 15:
    print('*')
else:
    print('x')
