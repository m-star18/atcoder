import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(readline())
if n == 1:
    print('Not Prime')
    exit()
if is_prime(n):
    print('Prime')
    exit()
n = list(str(n))
if n[-1] != '5' and int(n[-1]) % 2 == 1:
    cnt = 0
    for i in range(len(n)):
        cnt += int(n[i])
    if cnt % 3 != 0:
        print('Prime')
        exit()
print('Not Prime')
