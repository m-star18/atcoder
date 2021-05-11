import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime


q = int(readline())
primelist = makePrimeChecker(10 ** 5 + 2)
check = [0] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    if i % 2 == 1:
        if primelist[i] and primelist[(i + 1) // 2]:
            check[i] += 1
    check[i] += check[i - 1]
lr = [list(map(int, readline().split())) for _ in range(q)]
for l, r in lr:
    print(check[r] - check[l - 1])
