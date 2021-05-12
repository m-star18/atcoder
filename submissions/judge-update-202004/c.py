import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def search(a, b, c):
    if a == 1 and b == c == 0:
        return 1
    cnt = 0
    if c > 0:
        cnt += search(a, b, c - 1)
    if b > c:
        cnt += search(a, b - 1, c)
    if a > b:
        cnt += search(a - 1, b, c)
    return cnt


a = list(map(int, readline().split()))
print(search(*a))
