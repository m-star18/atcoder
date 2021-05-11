import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
r = sorted(list(map(int, readline().split())), reverse=True)
r = r[:k]
ans = 0
for i in range(1, k + 1):
    ans += r[i - 1] / (2 ** i)
print(ans)
