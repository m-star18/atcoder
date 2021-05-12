import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a, b = map(int, readline().split())
c = int(readline())
d = [int(readline()) for _ in range(n)]
d.sort(reverse=True)
ans = c // a
for dd in d:
    a += b
    c += dd
    ans = max(ans, c // a)
print(ans)
