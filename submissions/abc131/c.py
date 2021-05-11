import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

a, b, c, d = map(int, readline().split())
print((b - a + 1) - (b // c + b // d) + ((a - 1) // c + (a - 1) // d) + b // (c * d // gcd(c, d)) - (a - 1) // (c * d // gcd(c, d)))
