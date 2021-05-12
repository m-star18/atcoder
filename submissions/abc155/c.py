import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(readline())
s = [input() for i in range(n)]
check = list(Counter(s).items())
check.sort(key=lambda x: (-x[1], x[0]))
max_a = check[0][1]
for k, v in check:
    if v != check[0][1]:
        break
    print(k)
