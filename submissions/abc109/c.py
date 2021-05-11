import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

n, x = map(int, readline().split())
xx = list(map(int, readline().split()))
gcd_ans = abs(x - xx[0])
for i in range(1, n):
    gcd_ans = gcd(gcd_ans, abs(x - xx[i]))
print(gcd_ans)
