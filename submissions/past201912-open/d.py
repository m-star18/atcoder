import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(readline())
a = [int(readline()) for _ in range(n)]
b = set([(i + 1) for i in range(n)])
if b == (set(a) & b):
    print('Correct')
else:
    y = list(b - set(a))[0]
    x = Counter(a).most_common()[0][0]
    print(x, y)
