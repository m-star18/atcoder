import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def check(n):
    if n == 0:
        return ''
    if n % 2 == 0:
        return check(n // (-2)) + '0'
    return check((n - 1) // (-2)) + '1'


n = int(readline())
if n == 0:
    print(0)
else:
    print(check(n))
