import sys
input = sys.stdin.readline


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        if len(make_divisors(i)) == 8:
            cnt += 1

print(cnt)
