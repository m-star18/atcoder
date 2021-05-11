import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

n = int(readline())
ab = [list(map(int, readline().split())) for _ in range(n)]
check = ab.pop(0)
for a, b in ab:
    a_0 = gcd(check[0], a)
    b_0 = gcd(check[0], b)
    if a_0 < b_0:
        check[0] = b_0
    else:
        check[0] = a_0
    a_1 = gcd(check[1], a)
    b_1 = gcd(check[1], b)
    if a_1 < b_1:
        check[1] = b_1
    else:
        check[1] = a_1
print(max(check))
