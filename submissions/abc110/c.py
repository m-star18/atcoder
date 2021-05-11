import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

s = sorted(Counter(list(readline().rstrip().decode())).values())
t = sorted(Counter(list(readline().rstrip().decode())).values())
if s == t:
    print('Yes')
else:
    print('No')
