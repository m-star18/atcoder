import sys
import math
input = sys.stdin.readline


def eratosthenes(limit):
    if limit == 1:
        return []
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


n = int(input())
ans = len(eratosthenes(n - 1))
print(ans)
