import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
ans = float('inf')
for i in range(-100, 101):
    v = 0
    for aa in a:
        v += pow(aa - i, 2)
    ans = min(ans, v)
print(ans)
