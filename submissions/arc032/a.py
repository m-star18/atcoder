import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


# nの素数判定
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(readline())
if is_prime((n * (n + 1) // 2)):
    print('WANWAN')
else:
    print('BOWWOW')
