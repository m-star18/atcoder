import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, t = map(int, readline().split())
memo = 0
ab = []
for i in range(n):
    a, b = map(int, readline().split())
    memo += b
    ab.append(a - b)
ab.sort()
if memo > t:
    print(-1)
    exit()
for i, check in enumerate(ab):
    memo += check
    if memo > t:
        print(n - i)
        exit()
print(0)
