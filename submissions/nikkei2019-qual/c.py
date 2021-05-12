import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ab = []
ans = 0
for _ in range(n):
    a, b = map(int, readline().split())
    ab.append(a + b)
    ans -= b
ab.sort(reverse=True)
ans += sum(ab[::2])
print(ans)
