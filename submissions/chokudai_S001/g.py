import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
ans = ''
mod = 10 ** 9 + 7
for aa in a:
    ans += str(aa)
print(int(ans) % mod)
