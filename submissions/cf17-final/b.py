import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

s = read().rstrip().decode()
if max(Counter(list(s)).values()) <= (len(s) + 2) // 3:
    print('YES')
else:
    print('NO')
