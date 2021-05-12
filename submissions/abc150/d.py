import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
for i in range(n):
    a[i] //= 2
lcm_memo = 1
for i in range(n):
    lcm_memo *= a[i] // gcd(lcm_memo, a[i])
    if lcm_memo > m:
        print(0)
        exit()
for i in range(n):
    if (lcm_memo // a[i]) % 2 == 0:
        print(0)
        exit()
print(1 + (m - lcm_memo) // (lcm_memo * 2))
