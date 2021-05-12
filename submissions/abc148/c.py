import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

a, b = map(int, readline().split())
print(a * b // gcd(a, b))
