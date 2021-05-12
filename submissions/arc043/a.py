import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, readline().split())
s = [int(readline()) for _ in range(n)]
v = max(s) - min(s)
if v == 0:
    print(-1)
    exit()
p = b / v
q = (n * a - sum(s) * p) / n
print(p, q)
