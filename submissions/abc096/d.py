import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import math


def eratosthenes(limit):
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


n = int(readline())
prime_list = eratosthenes(55555)
ans = []
cnt = 0
for check in prime_list:
    if check % 5 == 1 and check > 10:
        ans.append(check)
        cnt += 1
        if cnt == n:
            print(*ans)
            exit()
