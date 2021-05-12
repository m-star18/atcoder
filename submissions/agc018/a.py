import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

n, k = map(int, readline().split())
a = list(map(int, readline().split()))
gcd_a = a[0]
for i in range(1, n):
    gcd_a = gcd(a[i], gcd_a)
if k % gcd_a == 0 and k <= max(a):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
