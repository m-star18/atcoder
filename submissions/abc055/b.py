import sys
input = sys.stdin.readline


def factorial_cor(n):
    fact = 1
    for integer in range(1, n + 1):
        if fact > 10 ** 9 + 7:
            fact %= 10 ** 9 + 7
        fact *= integer

    return fact


n = int(input())

ans = factorial_cor(n) % (10 ** 9 + 7)
print(ans)
