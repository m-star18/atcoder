import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import math
from bisect import bisect_left

def eratosthenes(limit):
    limit += 10 ** 3
    A = [i for i in range(2, limit + 1)]
    P = []

    for i in range(limit):
        prime = min(A)

        if prime > math.sqrt(limit):
            break

        P.append(prime)
        for j in range(limit):
            if j >= len(A):
                break
            if A[j] % prime == 0:
                A.pop(j)
                continue

    for a in A:
        P.append(a)

    return P


x = int(readline())
ans = eratosthenes(x)
print(ans[bisect_left(ans, x)])
