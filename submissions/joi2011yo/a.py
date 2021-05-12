import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a = sum([int(readline()) for i in range(4)])
print(a // 60)
print(a % 60)
