import sys
input = sys.stdin.readline


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


n = int(input())
if len(prime_decomposition(n)) == 1:
    print('YES')
else:
    print('NO')
