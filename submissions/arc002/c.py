import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product, combinations

n = int(readline())
w = readline().rstrip().decode() + '!'
memo = combinations(product(('A', 'B', 'X', 'Y'), repeat=2), 2)
ans = float('inf')
for x, y in memo:
    cnt = 0
    index = 0
    for i in range(n):
        if (w[index] == x[0] and w[index + 1] == x[1]) or (w[index] == y[0] and w[index + 1] == y[1]):
            index += 1
        index += 1
        cnt += 1
        if index >= n:
            break
    if ans > cnt:
        ans = cnt
print(ans)
