import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = 1000 - int(read())
ans = 0
k = [500, 100, 50, 10, 5, 1]
for check in k:
    ans += n // check
    n %= check
print(ans)
