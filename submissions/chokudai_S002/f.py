import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ab = set()
for i in range(n):
    a, b = map(int, readline().split())
    if b < a:
        ab.add((b, a))
    else:
        ab.add((a, b))
print(len(ab))
