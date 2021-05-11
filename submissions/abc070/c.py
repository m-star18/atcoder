import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

n = int(readline())
t = [int(readline()) for _ in range(n)]
ans = t[0]
for tt in t:
    ans = ans * tt // gcd(ans, tt)
print(ans)
