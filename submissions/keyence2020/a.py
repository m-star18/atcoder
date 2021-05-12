import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import math

h = int(readline())
w = int(readline())
n = int(readline())
ans = min(math.ceil(n / h), math.ceil(n / w))
print(ans)
