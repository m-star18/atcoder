import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

n, *a = map(int, read().split())
memo = 1
cnt = 0
mod = 10 ** 9 + 7
for aa in a:
    q = memo * aa // gcd(memo, aa)
    cnt *= q // memo
    memo = q
    cnt += q // aa
print(cnt % mod)
