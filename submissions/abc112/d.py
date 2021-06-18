import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n, m = map(int, readline().split())
if is_prime(m):
    if n == 1:
        print(m)
    else:
        print(1)
    exit()
for i in range(m // n, 0, -1):
    if m % i == 0:
        print(i)
        exit()
