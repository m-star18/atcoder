import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from decimal import Decimal

a, b = map(float, readline().split())
a = Decimal(str(a))
b = Decimal(str(b))
print(int(a * b))
