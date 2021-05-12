import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


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
divisors = make_divisors(n)
if sum(divisors) > 2 * n:
    print('Abundant')
elif sum(divisors) == 2 * n:
    print('Perfect')
else:
    print('Deficient')
