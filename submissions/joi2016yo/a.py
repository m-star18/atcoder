import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = [int(readline()) for _ in range(4)]
c = max([int(readline()) for _ in range(2)])
print(sum(s) - min(s) + c)
