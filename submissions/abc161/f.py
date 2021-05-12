import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from copy import deepcopy


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
ans = len(make_divisors(n - 1))
for check in make_divisors(n):
    if check == 1:
        continue
    nn = deepcopy(n)
    while nn % check == 0:
        nn //= check
    if nn % check == 1:
        ans += 1
print(ans - 1)
