import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ans = 0
for _ in range(n):
    abcde = list(map(int, readline().split()))
    ans = max(ans, sum(abcde[:-1]) + abcde[-1] * 110 / 900)
print(ans)
