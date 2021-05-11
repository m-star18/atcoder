import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, readline().split())


def check(n):
    if n < 0:
        return 0
    q, r = divmod(n, 10)
    q_str = str(q)
    if ('4' in q_str) or ('9' in q_str):
        return check(q - 1) * 8
    x = r + 1
    if r >= 4:
        x -= 1
    if r >= 9:
        x -= 1
    return x + check(q - 1) * 8


print(b - a + 1 - (check(b) - check(a - 1)))
