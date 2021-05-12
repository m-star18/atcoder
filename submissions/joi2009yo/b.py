import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

w = sorted([int(readline()) for _ in range(10)], reverse=True)
k = sorted([int(readline()) for _ in range(10)], reverse=True)
print(sum(w[0:3]), sum(k[0:3]))
