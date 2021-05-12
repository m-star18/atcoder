import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import gcd

n, q = map(int, readline().split())
a = list(map(int, readline().split()))
s = list(map(int, readline().split()))
cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = gcd(cumsum[i], a[i])
for i in s:
    if gcd(cumsum[n], i) != 1:
        print(gcd(cumsum[n], i))
        continue
    low = 0
    high = n
    while low + 1 < high:
        mid = (low + high) // 2
        if gcd(cumsum[mid], i) == 1:
            high = mid
        else:
            low = mid
    print(high)
