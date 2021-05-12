import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

h, w = map(int, readline().split())
a = []
for i in range(h):
    a += list(readline().rstrip().decode())
counter = Counter(a).values()
check = [1, h // 2 + w // 2, (h // 2) * (w // 2)]
if h % 2 == 0:
    check[0] = 0
    check[1] -= w // 2
if w % 2 == 0:
    check[0] = 0
    check[1] -= h // 2
for v in counter:
    if check[2] < v // 4:
        v -= 4 * check[2]
        check[2] = 0
    else:
        check[2] -= v // 4
        v %= 4
    if check[1] < v // 2:
        v -= 2 * check[1]
        check[1] = 0
    else:
        check[1] -= v // 2
        v %= 2
    check[0] -= v
print('Yes' if all(check[i] == 0 for i in range(3)) else 'No')
