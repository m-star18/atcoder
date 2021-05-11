import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import floor


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


n = int(readline())
prime_list = make_divisors(n)
ans = 0
prime_list.remove(1)
for i in range(len(prime_list)):
    prime_list[i] -= 1
    if floor(n / prime_list[i]) == n % prime_list[i]:
        ans += prime_list[i]
print(ans)
