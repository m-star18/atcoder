import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n, m, *a = map(int, read().split())
counter = Counter(a).most_common()[0]
if counter[1] > n // 2:
    print(counter[0])
else:
    print('?')
