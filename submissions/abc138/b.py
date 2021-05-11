import sys
from fractions import Fraction
input = sys.stdin.readline


def inverse(f):
    return Fraction(f.denominator, f.numerator)


n = int(input())
a = list(map(int, input().split()))
sum_a = 0
for i in range(n):
    sum_a += Fraction(1, a[i])
print(float(inverse(sum_a)))
