import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from numba import njit


@njit
def main(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i * (n // i) * (n // i + 1) // 2
    print(ans)


if __name__ == '__main__':
    n = int(readline())
    main(n)
