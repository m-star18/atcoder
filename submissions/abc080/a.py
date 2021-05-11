# sys.stdin.readline()
import sys
import math
input = sys.stdin.readline

n, a, b = map(int, input().split())
print(min(n*a, b))
