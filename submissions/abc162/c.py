import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

from math import gcd

k = int(readline())
cnt = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        gcd_ans = gcd(i, j)
        for l in range(1, k + 1):
            cnt += gcd(l, gcd_ans)
print(cnt)
