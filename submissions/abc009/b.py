import sys
import math
input = sys.stdin.readline

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
ans_a = list(set(a))
ans_a.sort()
print(ans_a[len(ans_a)-2])
