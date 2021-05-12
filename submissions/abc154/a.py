import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s, t = input().split()
a, b = map(int, input().split())
u = input()
if s == u:
    print(a - 1, b)
else:
    print(a, b - 1)
